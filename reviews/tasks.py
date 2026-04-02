import logging
import time
from datetime import timedelta

from celery import shared_task
from django.utils import timezone

from reviews.models import Review

logger = logging.getLogger(__name__)


def enqueue_review_processing(review_id, queue):
    try:
        if queue == "light":
            return normalize_review_text.apply_async(args=[review_id], queue=queue)
        else:
            return process_review_task.apply_async(args=[review_id], queue=queue)
    except Exception:
        Review.objects.filter(pk=review_id).update(is_verified=False)
        logger.exception(f"Review {review_id} failed permanently")
        return None


@shared_task(bind=True, max_retries=3, default_retry_delay=10)
def process_review_task(self, review_id):
    try:
        review = Review.objects.get(pk=review_id)
    except Review.DoesNotExist:
        logger.warning(f"Review {review_id} does not exist")
        return

    logger.info(f"Processing review {review_id}")

    try:
        time.sleep(5)

        review.is_verified = True
        review.save()

        logger.info(f"Review {review_id} processed successfully!")
        return {"status": "completed", "review_id": review_id}

    except Exception as exc:
        if self.request.retries >= self.max_retries:
            logger.exception(f"Review {review_id} failed permanently!")
            raise

        raise self.retry(exc=exc)


@shared_task
def normalize_review_body(review_id):
    review = Review.objects.get(pk=review_id)

    review.body = review.body.capitalize()
    review.save(update_fields=['body'])

    logger.info(f"Review {review_id} normalized")
    return {"status": "updated"}


@shared_task
def delete_old_reviews():
    cutoff = timezone.now() - timedelta(minutes=10)
    old_reviews = Review.objects.filter(created_at__lt=cutoff)

    count = old_reviews.count()
    old_reviews.delete()

    logger.info(f"Deleted {count} old reviews")
    return count
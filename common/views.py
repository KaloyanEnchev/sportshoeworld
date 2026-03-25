from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views import View
from django.db.models import Count

from accounts.forms import ProfileForm
from common.models import Like
from shoes.models import Shoe, Category

class HomeView(View):
    def get(self, request) -> HttpResponse:
        context = {"form": ProfileForm()}

        latest_shoes_qs = Shoe.objects.order_by('-created_at')[:3]

        context.update({
            "total_shoes": Shoe.objects.count(),
            "newest_shoe": latest_shoes_qs.first(),
            "most_liked": Shoe.objects.annotate(like_count=Count('like'))
            .filter(like_count__gt=0)
            .order_by('-like_count')[:3],
            "latest_shoes": latest_shoes_qs,
            "categories": Category.objects.all(),
        })

        return render(request, 'common/home_page.html', context)


def like_functionality(request, photo_pk: int) -> HttpResponse:
    like_object = Like.objects.filter(to_photo_id=photo_pk).first()

    if like_object:
        like_object.delete()
    else:
        Like.objects.create(
            to_photo_id=photo_pk,
        )

    return redirect(request.META.get('HTTP_REFERER') + f'#{photo_pk}')

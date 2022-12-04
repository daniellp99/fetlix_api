from rest_framework.routers import DefaultRouter

from series.api.views import SeriesViewset, EpisodesViewset

router = DefaultRouter()

router.register(prefix='series', basename='series', viewset=SeriesViewset)
router.register(prefix='episodes', basename='episodes', viewset=EpisodesViewset)
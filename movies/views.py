import datetime
from statistics import median
from typing import List, Optional

from django.shortcuts import get_object_or_404
from django.utils import timezone
from ninja import NinjaAPI, Schema, FilterSchema, Query
from ninja.pagination import paginate, PageNumberPagination
from pydantic import Field

from .models import Movie

api = NinjaAPI(
    title="DIVELIT task",
    description="movie rate backend"
)


class MovieSchemaIn(Schema):
    name: str
    rate: int


class MovieSchemaOut(Schema):
    id: int
    added_at: datetime.datetime
    name: str
    rate: int


class MovieSchemaFilter(FilterSchema):
    name: Optional[str] = Field(None, q='name__icontains')
    rate: Optional[int] = None
    added_at: Optional[datetime.datetime] = None


@api.get("get-all", response=List[MovieSchemaOut])
@paginate(PageNumberPagination)
def movies_list(request, filters: MovieSchemaFilter = Query(...)):
    queryset = Movie.objects.all()
    movies = filters.filter(queryset)
    return list(movies.order_by("-rate"))


@api.post("save")
def save_movie(request, movie: MovieSchemaIn):
    new_movie = Movie.objects.create(
        name=movie.name,
        rate=movie.rate,
    )
    return {'successfully_saved': new_movie.name}


@api.patch("update/{movie_id}")
def update_movie(request, movie_id: int, new_movie_data: MovieSchemaIn):
    movie = get_object_or_404(Movie, id=movie_id)
    movie.name = new_movie_data.name
    movie.rate = new_movie_data.rate
    movie.added_at = timezone.now()
    movie.save()
    return {'successfully_saved': movie.name}


@api.delete("delete/{movie_id}")
def delete_movie(request, movie_id: int):
    movie = get_object_or_404(Movie, id=movie_id)
    movie.delete()
    return {"successfully_deleted": movie.name}


@api.get("stats")
def get_stats(request):
    all_rates = list(Movie.objects.all().values_list("rate", flat=True))
    stats = {
        "movies_count": len(all_rates),
        "highest_rate": max(all_rates),
        "smallest_rate": min(all_rates),
        "median_rate": median(all_rates),
    }
    return stats

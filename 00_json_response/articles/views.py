from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import render
from django.http.response import JsonResponse, HttpResponse
from django.core import serializers
from .serializers import ArticleSerializer
from .models import Article

# Create your views here.
def article_html(request):
    articles = Article.objects.all()
    context = {
        'articles': articles,
    }
    return render(request, 'articles/article.html', context)


def article_json_1(request):
    # 모델 객체를 조회한다
    articles = Article.objects.all()
    # 데이터를 퓨어한 파이썬 객체로 변환 (전처리 과정)
    articles_json = []

    for article in articles:
        articles_json.append(
            {
                'id': article.pk,
                'title': article.title,
                'content': article.content,
                'created_at': article.created_at,
                'updated_at': article.updated_at,
            }
        )
    # JSON 문자열 포멧으로 응답
    return JsonResponse(articles_json, safe=False)  # safe=False가 있는 이유는 리스트 형태여도 정상적으로 전달 되기 때문


def article_json_2(request):
    # Django 라이브러리에서 지원하는 시리얼라이저를 지웒는 방법
    # 시리얼라이쩌(serializers = 직렬화) : 복잡하게 구성되어 있는 리소스(데이터)들을 평이한 데이터로 재구성한다.
    articles = Article.objects.all()
    data = serializers.serialize('json', articles)

    # data = '{"name":"홍길동" ,"score" : 100,"age" : 17}'
    return HttpResponse(data, content_type='application/json')


# @api_view(['GET'])
@api_view()
def article_json_3(request):
    articles = Article.objects.all()
    serializer = ArticleSerializer(articles, many=True)
    return Response(serializer.data)

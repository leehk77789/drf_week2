from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.generics import get_object_or_404
from articles.models import Article
from articles.serializers import ArticleSerializer

@api_view(['GET', 'POST'])
def articleAPI(request):
    if request.method == 'GET':
        articles = Article.objects.all()
        #여러 자료를 넣을 때에는 many=True 넣어줘야함
        serializer = ArticleSerializer(articles, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        else:
            print(serializer.errors)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def articleDetailApi(request, article_id):
    #게시물 가져오기
    if request.method == 'GET':
        article = get_object_or_404(Article, id=article_id)
        serializer = ArticleSerializer(article)
        return Response(serializer.data)
    #게시물 수정
    elif request.method == 'PUT':
        article = get_object_or_404(Article, id=article_id)
        serializer = ArticleSerializer(article, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
    
    #게시물 삭제
    elif request.method == 'DELETE':
        article = get_object_or_404(Article, id=article_id)
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
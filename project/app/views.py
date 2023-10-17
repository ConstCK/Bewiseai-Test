from django.db import IntegrityError
from django.http import HttpRequest
from django.utils.datastructures import MultiValueDictKeyError
from rest_framework.decorators import api_view
from rest_framework.response import Response
import requests

from .models import Quiz
from .serializers import QuizSerializer


@api_view(["get", "post"])
def get_data(request: HttpRequest) -> Response:
    if request.method == "POST":
        try:
            number: int = request.POST["questions_num"]
        except MultiValueDictKeyError:
            return Response("Ошибка запроса...")

        while True:
            try:
                r: requests.Response = requests.get("https://jservice.io/api/random", params={"count": number})
                data: dict = r.json()
                counter: int = len(data)
                if data:
                    for i in data:
                        try:
                            Quiz.objects.create(question_id=i["id"], question=i["question"], answer=i["answer"],
                                                created_at=i["created_at"])
                            counter -= 1
                            if counter == 0:
                                try:
                                    obj = Quiz.objects.last()
                                    serializer = QuizSerializer(obj)
                                    result = serializer.data
                                    return Response(result)
                                except:
                                    return Response({})

                        except IntegrityError:
                            continue
                        number = counter
                else:
                    return Response("Данные отсутствуют...")

            except:
                return Response("Ошибка запроса...")

    else:
        return Response("Ошибка запроса...")

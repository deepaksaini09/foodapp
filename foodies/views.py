import json
import sys
from django.shortcuts import render
from django.shortcuts import HttpResponse
from foodies.dBService import dBServices
from foodies.culumnName import columnNames
from foodapp.serializeAndDeserialize import convertPythonDataIntoJsonData

dBServicesObj = dBServices()
columnNamesObj = columnNames()


def home(request):
    return HttpResponse('hi saini')


def bestRestaurantsByRatings(request):
    try:
        orderByRating = True
        orderByCfo = True
        orderByCft = True
        orderByDistance = True
        orderByDeliveryTime = True
        orderByOfferAvailable = True
        orderByVotes = True
        data, error = dBServicesObj.getAllZomatoRestaurantsByRating(orderByRating, orderByDistance, orderByCft,
                                                                    orderByCfo, orderByOfferAvailable,
                                                                    orderByDeliveryTime, orderByVotes)
        if error:
            return HttpResponse('error occurred during fetch all restaurant by rating')
        column = columnNamesObj.columnNameForRestaurantByRating()
        jsonDataOfRestaurantsByRating, error = convertPythonDataIntoJsonData(data, column)
        if error:
            return HttpResponse('error occurred during converting key value pair')
        data = {'ratingRestaurants': jsonDataOfRestaurantsByRating}
        data = json.dumps(data, default=str)
        return HttpResponse(data, content_type='application/json')
    except Exception as error:
        print(error)
        return HttpResponse('internal error in server')


def bestTrendingRestaurants(request):
    try:
        data, error = dBServicesObj.getAllTrendingRestaurants()
        if error:
            print("bestTrendingRestaurants: error occurred during fetch trending restaurants", error)
            return HttpResponse('bestTrendingRestaurants: error occurred during fetch trending restaurants')
        column = columnNamesObj.columnNameForRestaurantByRating()
        jsonDataOfRestaurantsByTrending, error = convertPythonDataIntoJsonData(data, column)
        if error:
            return HttpResponse('bestTrendingRestaurants:error occurred during converting key value pair')
        data = {'ratingRestaurants': jsonDataOfRestaurantsByTrending}
        data = json.dumps(data, default=str)
        return HttpResponse(data, content_type='application/json')
    except Exception as error:
        print(error)
        return HttpResponse('bestTrendingRestaurants: internal server error')

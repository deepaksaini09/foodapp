import sys

from django.db import connection


class dBServices:
    def __init__(self):
        self.conn = connection
        self.cursor = connection.cursor()

    # ------------------------------------------ get restaurants details by ratings --------------------------------

    def getAllZomatoRestaurantsByRating(self, orderByRating, orderByDistance, orderByCft, orderByCfo,
                                        orderByOfferAvailable, orderByDeliveryTime, orderByVotes):
        try:
            # SQL
            SQL = """select restaurants, type, rating, votes, cft, cfo, address, locality_url, timing, 
                            detail_page_url, distance, delivery_time, restaurants_image, offers, address_name 
                        from restaurants_zomato_dev """
            if orderByRating:
                SQL += """ order by rating desc"""
            if orderByVotes:
                SQL += """ ,votes desc"""
            if orderByOfferAvailable:
                SQL += """ ,offers """
            if orderByCft:
                SQL += """ ,cft desc"""
            if orderByCfo:
                SQL += """ ,cfo desc"""
            if orderByDistance:
                SQL += """ ,distance """
            if orderByDeliveryTime:
                SQL += """ ,delivery_time """
            SQL += """ desc"""
            print(SQL, "*******************")
            self.cursor.execute(SQL)
            restaurantsData = self.cursor.fetchall()
            if restaurantsData:
                self.conn.close()
                return restaurantsData, None
            self.conn.close()
            return False
        except Exception as error:
            return None, error

    # --------------------- get all trending Restaurants -------------------------------------------------
    def getAllTrendingRestaurants(self):
        try:
            # SQL
            SQL = """ select  distinct
                               rzd.restaurants,
                               rzd.type,
                               rzd.rating,
                               rzd.votes,
                               rzd.cft,
                               rzd.cfo,
                               rzd.address,
                               rzd.locality_url,
                               rzd.timing,
                               rzd.detail_page_url,
                               rzd.distance,
                               rzd.delivery_time,
                               rzd.restaurants_image,
                               rzd.offers,
                               rzd.address_name,
                               rpozd.textData,
                               rpozd.recently_placed
                        from restaurants_zomato_dev rzd
                                 join recently_placed_order_zomato_dev rpozd on rzd.id = rpozd.restaurant_id
                        where rpozd.recently_placed is not null
                        order by recently_placed desc limit 10;

                 """
            self.cursor.execute(SQL)
            data = self.cursor.fetchall()
            if data:
                self.conn.close()
                return data, None
            self.conn.close()
            return False, None
        except Exception as error:
            print(error)
            return None, error

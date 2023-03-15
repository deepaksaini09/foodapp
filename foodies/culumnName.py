class columnNames:
    def __init__(self):
        pass

    @staticmethod
    def columnNameForRestaurantByRating():
        try:
            column = [
                'restaurants', 'type', 'rating', 'votes', 'cft', 'cfo', 'address', 'locality_url', 'timing',
                'detail_page_url', 'distance', 'delivery_time', 'restaurants_image', 'offers', 'address_name'
            ]
            return column
        except Exception as error:
            print(error)

    def columnNameForTrendingRestaurants(self):
        try:
            column = self.columnNameForRestaurantByRating()
            column.extend(['textData', 'recently_placed'])
            return column
        except Exception as error:
            print(error)

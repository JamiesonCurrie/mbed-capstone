# mbed-capstone
Meta Backend Developer Capstone - LittleLemonAPI

I split the API functionality from the restaurant web page functionality.  Most of the files for testing the project are found in LittleLemonAPI/ app directory.


# Project Files

* littlelemon/
    * settings.py       - project settings
    * urls.py           - project end points
    * tests/
      * test_models.py  - test the MenuItem model
      * test_views.py   - test the MenuItem Views
* LittleLemonAPI/
    * models.py      - MenuItem and Bookings models
    * admin.py       - register models
    * serializers.py - MenuItem and Bookings Serializers
    * views.py       - Bookings and MenuItem API Viewsets
    * urls.py        - API end points
* restaurant/
    * templates/ - web page HTML templates
    * static/    - static assets
    * urls.py    - web page end points
    * views.py   - web page views

# End Points:
* littlelemon.urls
    * /admin
    * /auth/
      * djoser.urls
      * djoser.urls.authtoken
* LittleLemonAPI.urls:
  * /api/api-token-auth
  * /api/users
  * /api/users/\<int:pk\>
  * /api/categories
  * /api/categories/\<int:pk\>
  * /api/menu-items
  * /api/menu-items/\<int:pk\>
  * /api/bookings
  * /api/bookings/\<str:reservation_date\>
* restaurant.urls
  * /restaurant
  * /restaurant/about
  * /restaurant/menu
  * /restaurant/menu-item/\<int:pk\>
  * /restaurant/book
  * /restaurant/tables

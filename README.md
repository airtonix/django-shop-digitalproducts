django-shop-digitalproducts
===========================

Sell digital downloads with django-shop.

Goals for this project:

* Provide model mixins for (separately):

    * ability to specify shipping requirement on a per product instance
    * methods for accessing a products digital assets
        These could be fields on another model (like django-shop-configurableproduct)
        or a field on the same model
    * securely storing digital assets

* provide a default product model that encompasses the above mixins into one ready to use model

* Provide view mixins for :

    * access to purchased assets via hashed url
    * timeframe limited access to purchased assets


Future Roadmap
==============

* Storage backend that emails compressed archive of assets
* Storage backend that password protects archive of assets
* Storage backend that communicates with configurable RESTful 
  api to generate a Product Key for the customer.
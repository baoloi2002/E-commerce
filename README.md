# E-commerce
E-commerce Website using Django

Thanks to [ThemeWagon](https://themewagon.com/themes/free-bootstrap-ecommerce-template-electro/) for providing the free template.



## Problem may occur:
1. When logging out in the admin panel encounters the 405 error, please change the block code below:
```html
<a href="{% url 'admin:logout' %}" class="dropdown-item">
    <i class="fas fa-users mr-2"></i> {% trans 'Log out' %}
</a>
```
to
```html
<form action="{% url 'admin:logout' %}" method="post">
    {% csrf_token %}
    <button type="submit" class="dropdown-item">
        <i class="fas fa-users mr-2"></i> {% trans 'Log out' %}
    </button>
</form>
```
in "`venv\Lib\site-packages\jazzmin\templates\admin\base.html`" file.


from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from netology.models import (
    Category,
    ConfirmEmailToken,
    Contact,
    Order,
    OrderItem,
    Parameter,
    Product,
    ProductInfo,
    ProductParameter,
    Shop,
    User,
)


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    """
    Панель управления пользователями
    """

    model = User
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("email", "password1", "password2"),
            },
        ),
    )
    fieldsets = (
        (None, {"fields": ("email", "password", "type")}),
        (
            "Personal info",
            {"fields": ("first_name", "last_name", "company", "position")},
        ),
        (
            "Permissions",
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                ),
            },
        ),
        ("Important dates", {"fields": ("last_login", "date_joined")}),
    )
    list_display = ("email", "first_name", "last_name", "is_staff")


@admin.register(Shop)
class ShopAdmin(admin.ModelAdmin):
    list_display = ["name", "url", "user", "state"]
    list_filter = ["state"]
    search_fields = [
        "name",
        "user__first_name",
        "user__last_name",
    ]


class ShopInline(admin.TabularInline):
    model = Shop.categories.through
    verbose_name = verbose_name_plural = "Магазины"


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    inlines = [ShopInline]
    list_display = ["name"]
    fieldsets = ((None, {"fields": ["name"]}),)
    search_fields = ["name"]


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ["name", "category"]
    search_fields = ["name"]


@admin.register(ProductInfo)
class ProductInfoAdmin(admin.ModelAdmin):
    list_display = ["product", "model", "shop", "quantity", "price", "price_rrc"]
    search_fields = ["product__name"]


@admin.register(Parameter)
class ParameterAdmin(admin.ModelAdmin):
    list_display = ["name"]


@admin.register(ProductParameter)
class ProductParameterAdmin(admin.ModelAdmin):
    list_display = ["product_info", "parameter", "value"]
    search_fields = ["product_info__model", "value"]


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ["create_time_display", "state", "user", "contact"]
    search_fields = ["user"]
    list_filter = ["state"]

    def create_time_display(self, obj):
        return obj.dt.strftime("%d-%m-%Y %H:%M:%S")


@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = [
        "order",
        "product_info",
        "quantity",
    ]
    search_fields = ["order__dt"]


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ["user", "city", "phone"]
    list_filter = ["city"]
    search_fields = [
        "user__first_name",
        "user__last_name",
    ]


@admin.register(ConfirmEmailToken)
class ConfirmEmailTokenAdmin(admin.ModelAdmin):
    list_display = (
        "user",
        "key",
        "created_at",
    )

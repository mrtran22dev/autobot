common = {
    'button': {
        'sign_in': '#account-sign-in',
        'signin_sidebar': '[data-test="accountNav-signIn"]',
        'search': '[data-test="@web/Search/SearchButton"]',
        'cart_icon': '[data-test="@web/CartIcon"]',
        'delivery': '[data-test="fulfillment-cell-delivery"]',
        'add_to_cart_sidebar': '//div[@data-test="content-wrapper"]//button[text()="Add to cart"]',
        'close_sidebar': '[aria-label="close"] >> nth=2',
        'add_address_sidebar': '[data-test="address-block-action-button"]',
        'first_name_sidebar': '#first_name',
        'last_name_sidebar': '#last_name',
        'address_sidebar': '#address_line1',
        'zip_sidebar': '#zip_code',
        'city_sidebar': '#city',
        'state_sidebar': '#state option[value="CA"]',
        'phone_sidebar': '#phone_number',
        'save_address_sidebar': '[data-test="primary-save-button"]',
        'skip': '//a[text()="Skip"]',
        'decline_coverage_sidebar': '[data-test="espDrawerContent-declineCoverageButton"]',
        'continue_membership_sidebar': '#save-membership-button',
    },
    'input': {
        'search': '#headerPrimary #search'
    }
}

landing = {
    'button': {
        'categories': '#headerPrimary >> div:nth=2',
    },
    'validate': {
        'element': '[data-test="pictureNavigation"] ul li >> nth=1'     # Electronics categories present
    }
}

products_list = {
    'button': {
        'product_nth': '[data-test="product-grid"] [data-test="@web/ProductCard/ProductCardImage"] >> nth=%s',
        'add_to_cart_first_item': '[id^="addToCartButtonOrTextIdFor"] >> nth=1',
        'sort': '[data-test="facet-button-Sort"]',
        'filter_bar': '(//*[@data-test="lp-filterBar"])[1]//*[contains(text(), "%s")]',
        'sidebar_apply': '//button[text()="Apply"]'
    },
    'input': {
        'sidebar_filter_menu': '//*[@data-test="content-wrapper"]//*[@class="h-padding-v-default"]//input',
        'sidebar_filter_min_price': '#minPriceValue',
        'sidebar_filter_max_price': '#maxPriceValue',
    },
    'list': {
        'sidebar_filter_menu': '//*[@data-test="content-wrapper"]//*[text()="%s"]',
        'items_price': '[data-test="current-price"]'
    },
    'validate': {
        'element': '[data-test="product-grid"] [data-test="@web/ProductCard/ProductCardImage"] >> nth=0'
    }
}

product = {
    'button': {
        'add_to_cart': '[data-module-type="ProductDetailFulfillment"] [id^=addToCartButtonOrTextId]',
        'delivery': '[data-test="fulfillment-cell-delivery"]',
    },
    'validate': {
        'element': '[id="pdp-product-title-id"]'
    }
}

login = {
    'input': {
        'user': '#username',
        'password': '#password',
    },
    'button': {
        'login': '#login',
    },
    'text': {
        'login_alert': '[data-test="authAlertDisplay"]',
    },
    'validate': {
        'element': '#username'
    }
}

cart = {
    'button': {
        'checkout': '[data-test="checkout-button"]',
        'delete_item': '[data-test="cartItem-deleteBtn"]',
    },
    'validate': {
        'element': '#cart-summary-heading'
    }
}

checkout = {
    'button': {
        'save_continue': '[data-test="primary-save-button"]',
        'place_order': '[data-test="placeOrderButton"]',
        'use_verified_address': '[data-test="useUnverifiedAddressButton"]',
        'address_edit': '[data-test="edit-shipping-button"]',
        'address_edit2': '[data-test="editButton"]',
    },
    'input': {
        'first_name': '#first_name',
        'last_name': '#last_name',
        'address': '#address_line1',
        'zip': '#zip_code',
        'city': '#city',
        'state': '#state',
        'phone': '#phone_number',
    },
    'validate': {
        'element': '[data-test="checkout-summary-container"]'
    }
}
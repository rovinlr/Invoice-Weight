{
    "name": "Invoice Weight",
    "summary": "Add net and total weight fields to sale and invoice lines",
    "version": "19.0.1.0.0",
    "category": "Sales",
    "author": "OpenAI",
    "website": "https://example.com",
    "license": "LGPL-3",
    "depends": ["sale_management", "account"],
    "data": [
        "views/sale_order_views.xml",
        "views/account_move_views.xml",
    ],
    "installable": True,
    "application": False,
}

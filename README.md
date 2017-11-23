# Mezaext

Extensions for mezzanine CMS

Пока не создан пакет в pypi, поэтому можно устанавливать альтернативным способом.
Пока не версионируется.

## Функциональность:

 * Добавляет тег редактируемого блока
 * Добавляет контактную форму с полями: имя, почта, телефон, текст
 * Выносим нужные шаблоны, сопряженные с клиентом regular-gulpfile

## Как ставить.

В INSTALLED_APPS добавляем 'mezaext'.

Делаем мигрейт.

Чтобы шаблоны работали, переопределяем TEMPLATES.DIRS: os.path.join(PROJECT_ROOT, 'mezaext', "templates") если установлено копированием.

```python
STATICFILES_DIRS = (os.path.join(PROJECT_ROOT, '..', 'client'),)

ADMIN_MENU_ORDER = (
    (
        "Content", (
            "pages.Page", "generic.ThreadedComment",
            (_("Media Library"), "media-library"),
            (u'Новости', "blog.BlogPost",),
            (u'Блоки', "mezaext.EditableBlock",),
        )
    ),
    ("Site", ("sites.Site", "redirects.Redirect", "conf.Setting")),
    ("Users", ("auth.User", "auth.Group",)),
)

PAGE_MENU_TEMPLATES = (
    #(1, u'Главное меню', "pages/menus/dropdown.html"),
    (1, u'Главное меню', "pages/menus/flat.html"),
)
```

Можно добавить SLUGIFY = 'pytils.translit.slugify'

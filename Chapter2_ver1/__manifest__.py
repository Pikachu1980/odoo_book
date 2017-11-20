{
    'name': 'To-Do Application',
    'description': 'Manage your personal To-Do tasks.',
    'author': 'Daniel Reis',
    'depends': ['base'],
    'application': True,
    # 我的資料夾名稱叫todo_app
    'data': [
        'security/ir.model.access.csv',
        'security/todo_access_rules.xml',
        'views/todo_view.xml',
        'views/todo_menu.xml',
    ],
}

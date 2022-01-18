{
    'name': "Attendance Logs",

    'summary': """
         Attendance Log for Employees
         """,

    'description': """
        
    """,

    'author': "GMSC IT TEAM",
    'website': "",
    'category': 'GMSC IT',
    'version': '12.0.1',
    'depends': ['base', 'hr_attendance'],
    'license': 'AGPL-3',

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/hr_attendance_log.xml'
    ],
}

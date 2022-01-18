{
    'name': "Hr Attendance Sheet Report",
    'summary': """
        Hr Attendance Sheet Report Summary
    """,
    'description': """
        Hr Attendance Sheet Report Description
    """,
    'category': "GMS Category",

    'depends': [
        'hr_attendance'
    ],
    'data': [
        # 'security/ir.model.access.csv',
        'views/hr_attendance_report_view.xml'
    ]

}
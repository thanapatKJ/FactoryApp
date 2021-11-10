from django.test import TestCase
from .models import User, WorkPlan

class UserTestCase(TestCase):
    def setUp(self):
        User.objects.create(
            username="SanChai",
            first_name="Sanchai",
            last_name="Jaiprom",
            email="sanchai.j@gmail.com",
            password="sanchaiapk",
            id_card="01123",
            roles="พนักงาน")
        
    def test_user_information(self):
        user = User.objects.get(username="SanChai")
        self.assertEqual(user.first_name ,'Sanchai')
        self.assertEqual(user.last_name ,'Jaiprom')
        self.assertEqual(user.email ,'sanchai.j@gmail.com')
        self.assertEqual(user.id_card ,'01123')
        self.assertEqual(user.roles ,'พนักงาน')
    
    
class WorkPlanTestCase(TestCase):
    def setUp(self):
        WorkPlan.objects.create(
            datetime="2021-10-16, 05:00 - 13:00",
            work_group = "ถอนขนไก่กะ 1",
            datetime_start = '2021-10-16 05:00:00',
            datetime_end = '2021-10-16 15:00:00',
            limit_worker = 40,
            limit_OT_worker= 10,
            limit_OT_hour = 2.5
        )

    def test_workplan_information(self):
        work = WorkPlan.objects.get(datetime="2021-10-16, 05:00 - 13:00")
        self.assertEqual(work.work_group ,'ถอนขนไก่กะ 1')
        # self.assertEqual(work.datetime_start ,'2021-10-16 05:00:00')
        # self.assertEqual(work.datetime_end ,'2021-10-16 15:00:00')
        self.assertEqual(work.limit_worker ,40)
        self.assertEqual(work.limit_OT_worker ,10)
        self.assertEqual(work.limit_OT_hour ,2.5)
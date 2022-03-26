from django.test import TestCase
from .models import Category,Location,Image

# Create your tests here.
class CategoryTestClass(TestCase):

    # Set up method
    def setUp(self):
        self.lewis=Category(name='lewis')

    # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.lewis,Category))

    # Testing Save Method
    def test_save_category(self):
        self.lewis.save_category()
        category = Category.objects.all()
        self.assertTrue(len(category) > 0)

    # Testing Delete Method
    def test_delete_category(self):
        self.lewis.save_category()
        self.lewis.delete_category()
        category = Category.objects.all()
        self.assertTrue(len(category) == 0)

class LocationTestClass(TestCase):

    # Set up method
    def setUp(self):
        self.eldoret=Location(location='Eldoret')

    # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.eldoret,Location))

    # Testing Delete Method
    def test_delete_location(self):
        self.eldoret.save_location()
        self.eldoret.delete_location()
        location = Location.objects.all()
        self.assertTrue(len(location) == 0)

    # Testing Save Method
    def test_save_location(self):
        self.eldoret.save_location()
        location = Location.objects.all()
        self.assertTrue(len(location) > 0)

class ImageTestClass(TestCase):

    # Set up method
    def setUp(self):
        # Creating a new category and saving it
        self.lewis=Category(name='lewis')
        self.lewis.save_category()

        # Creating a new location and saving it
        self.eldoret=Location(location='Eldoret')
        self.eldoret.save_location()

        self.new_image=Image(name='murgor',description='My photo',category=self.lewis,location=self.eldoret)
        self.new_image.save_image()

    def tearDown(self):
        Category.objects.all().delete()
        Location.objects.all().delete()
        Image.objects.all().delete()

    # Testing  instance
    def test_check_instance_variables(self):
        self.assertEqual(self.new_image.name, 'murgor')
        self.assertEqual(self.new_image.description, 'My photo')
        self.assertEqual(self.new_image.category, self.lewis)
        self.assertEqual(self.new_image.location, self.eldoret)

    # Testing Save Method
    def test_save_image(self):
        self.new_image.save_image()
        images = Image.objects.all()
        self.assertTrue(len(images) > 0)

    # Testing Delete Method
    def test_delete_image(self):
        self.new_image.save_image()
        self.new_image.delete_image()
        images = Image.objects.all()
        self.assertTrue(len(images) == 0)

    def test_get_image_by_id(self):
        image = Image.get_image_by_id(1)
        self.assertTrue(len(image) == 0)

    def test_search_by_category(self):
        image = Image.search_by_category(self.lewis)
        self.assertTrue(len(image))

    def test_filter_by_location(self):
        image = Image.filter_by_location(self.eldoret)
        self.assertTrue(image)

    

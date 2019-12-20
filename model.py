from django.db import models
from .mixins import TimeAuditModel
from django.contrib.postgres.fields import JSONField

class mall(TimeAuditModel):
    choose=(("Active","Active"),("Not Active","Not Active"))

    mall_name=models.CharField(max_length=50,verbose_name="Mall Name")
    mall_status=models.CharField(max_length=10,choices=choose,verbose_name="Mall Status")
    data = JSONField()
    mall_address=models.TextField(verbose_name="Address of Mall") 

    """
        Mall has multiple designers,so we use ManyToOne relationship
    
    """

    designer_key=models.ForeignKey('designer',on_delete=models.CASCADE,verbose_name="Mall Have Designer",related_name="malls",blank=True)

    class Meta:
        verbose_name = 'mall'
        verbose_name_plural = 'malls'
        db_table = 'mall'

    def __str__(self):
         return self.mall_name

class store(TimeAuditModel):
    choose=(("Active","Active"),("Not Active","Not Active"))

    store_name=models.CharField(max_length=50,verbose_name="Store Name")
    store_status=models.CharField(max_length=10,choices=choose,verbose_name="Store Status")
    store_description=models.CharField(max_length=100,verbose_name="Store Description")
    store_address=models.TextField(verbose_name="Address of Store") 
    
    """
        Store points towards mall and designer, so we use ManyToOne relationship

    """


    mall_key = models.ForeignKey(mall, on_delete=models.CASCADE,blank=True,verbose_name="Store Belongs To",related_name="stores")

    designer_key2 = models.ForeignKey('designer', on_delete=models.CASCADE,verbose_name="Store Have",related_name="DesignerStores")

    class Meta:
        verbose_name = 'store'
        verbose_name_plural = 'stores'
        db_table = 'store'

    def __str__(self):
          return self.store_name

class designer(TimeAuditModel):
    choose=(("Active","Active"),("Not Active","Not Active"))

    designer_name=models.CharField(max_length=50)
    designer_status=models.CharField(max_length=10,choices=choose)

    """  m2m field for designer and mall has both side depencies,
       'through' used for intermediate that you want to use 
    """
    mall_m2m=models.ManyToManyField(mall,through='store',verbose_name="Designer Belongs To")
    
    
    class Meta:

        verbose_name = 'designer'
        verbose_name_plural = 'designers'
        db_table = 'designer'

    def __str__(self):
          return self.designer_name



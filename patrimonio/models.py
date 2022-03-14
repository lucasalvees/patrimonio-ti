from django.db import models

class PatrimonioTipo(models.Model):
    descricao = models.CharField(verbose_name='Descrição', max_length=50)

    class Meta:
        db_table = 'patrimonio_tipo' 
        verbose_name = 'Patrimônio Tipo'

    def __str__(self):
        return self.descricao

class Patrimonio(models.Model):
    BM = 'BOM(USADO)'
    IN = 'INSERVIVEL'
    EM = 'EM MANUTENÇÃO'

    OC = 'OCIOSO'
    EU = 'EM USO'

    STATUSCONSERVACAO = (
        ("BM", "BOM(USADO)"),
        ("IN", "INSERVÍVEL"),
        ("EM", "EM MANUTENÇÃO")
    )
    STATUSOBJETO = (
        ("OC", "OCIOSO"),
        ("EU", "EM USO")
    )
    BEMEBSERH = (
        ("S", "SIM"),
        ("N", "NÃO")
    )

    patrimonio_tipo = models.ForeignKey(PatrimonioTipo, on_delete=models.CASCADE, verbose_name='Patrimônio Tipo')
    siads = models.IntegerField(verbose_name='Cód. SIADS')
    patrimonio_ebserh = models.IntegerField(verbose_name='Cód. Patrimônio EBSERH')
    patrimonio_uft = models.IntegerField(verbose_name='Cód. Patrimônio UFT')
    descricao = models.CharField(verbose_name='Descrição', max_length=150)
    marca = models.CharField(verbose_name='Marca', max_length=50)
    modelo = models.CharField(verbose_name='Modelo', max_length=50)
    data_aquisicao = models.DateField(verbose_name='Data de Aquisição', null=False)
    status_conservacao = models.CharField(verbose_name='Status de Conservação', choices=STATUSCONSERVACAO, max_length=2)
    status_obj = models.CharField(verbose_name='Status', choices=STATUSOBJETO, max_length=2)
    bem_ebserh = models.CharField(verbose_name='Bem EBSERH', choices=BEMEBSERH, max_length=1)

    class Meta:
        db_table = 'patrimonio'
        verbose_name = 'Patrimônio'

    def __str__(self):
        return "{} - {}, {} - {}".format(self.patrimonio_tipo.descricao, self.marca, self.modelo, self.status_obj)
from django.db import models

# Create your models here.

#Tabela UnidadeMedida
class UnidadeMedida(models.Model):
    descricao = models.CharField(max_length=50)
    unidadeMedida = models.CharField(max_length=15)
    flg = models.BooleanField()

    class Meta:
        verbose_name  = 'UnidadeMedida'
        verbose_name_plural = 'UnidadeMedidas'
        db_table = 'estoque_unidademedida'

    def __str__(self):
        return self.unidadeMedida

#Tabela Ambiente
class Ambiente(models.Model):
    descricao = models.CharField(max_length=70)
    flg = models.BooleanField()

    class Meta:
        verbose_name = 'Ambiente'
        verbose_name_plural = 'Ambientes'

    def __str__(self):
        return self.descricao

#Tabela Secao
class Secao(models.Model):
    descricao = models.CharField(max_length=70)
    flg = models.BooleanField()

    class Meta:
        verbose_name = 'Seção'
        verbose_name_plural = 'Seções'

    def __str__(self):
        return self.descricao

#Tabela Localizacao
class Localizacao(models.Model):
    descricao = models.CharField(max_length=70)
    flg = models.BooleanField()

    class Meta:
        verbose_name = 'Localizaçõa'
        verbose_name_plural = 'Localizações'

    def __str__(self):
        return self.descricao

#Tabela Grupo
class Grupo(models.Model):
    descricao = models.CharField(max_length=70)
    flg = models.BooleanField()

    class Meta:
        verbose_name = 'Grupo'
        verbose_name_plural = 'Grupos'

    def __str__(self):
        return self.descricao

#Tabela SubGrupo
class SubGrupo(models.Model):
    idGrupo = models.PositiveIntegerField()
    descricao = models.CharField(max_length=70)
    flg = models.BooleanField()
    grupo = models.ForeignKey(Grupo, on_delete=models.RESTRICT)

    class Meta:
        verbose_name = 'SubGrupo'
        verbose_name_plural = 'SubGrupos'

    def __str__(self):
        return self.descricao

#Tabela Produto
class Produto(models.Model):
    TIPO_INCENDIO_CHOICE = [
        (1, 'CLASSE A'),
        (2, 'CLASSE B'),
        (3, 'CLASSE C'),
        (4, 'CLASSE D')
    ]
    codigoBarra = models.CharField(max_length=100)
    descricao = models.CharField(max_length=100)
    precoCusto = models.DecimalField(max_digits=8, decimal_places=2)
    percentual = models.DecimalField(max_digits=5,decimal_places=2)
    precoVenda = models.DecimalField(max_digits=8, decimal_places=2)
    lote = models.CharField(max_length=30)
    quantidadeDisponivel = models.DecimalField(max_digits=8, decimal_places=2)
    quantidadeMinima = models.DecimalField(max_digits=8, decimal_places=2)
    quantidadeMaxima = models.DecimalField(max_digits=8, decimal_places=2)
    pesoLiquido = models.DecimalField(max_digits=8, decimal_places=2)
    pesoBruto = models.DecimalField(max_digits=8, decimal_places=2)
    temperaturaMinima = models.DecimalField(max_digits=5, decimal_places=2)
    temperaturaMaxima = models.DecimalField(max_digits=5, decimal_places=2)
    perecivel = models.BooleanField()
    promocao = models.BooleanField()
    precoPromocao = models.DecimalField(max_digits=8, decimal_places=2)
    marca = models.CharField(max_length=50)
    modelo = models.CharField(max_length=50)
    observacao = models.CharField(max_length=150)
    flg = models.BooleanField()
    ipi = models.DecimalField(max_digits=5, decimal_places=2)
    icms = models.DecimalField(max_digits=5, decimal_places=2)
    aliquota = models.DecimalField(max_digits=5, decimal_places=2)
    consignacao = models.BooleanField()
    tipoIncendio = models.PositiveIntegerField(choices=TIPO_INCENDIO_CHOICE) #Recebe um choice, ou seja, valor escolhido
    # fabricante = models.PositiveIntegerField()
    fabricanteT = models.CharField(max_length=80)
    #fornecedor = models.PositiveIntegerField()
    fornecedorT = models.CharField(max_length=80)
    # unidadeMedN = models.PositiveIntegerField()
    unidadeMed = models.CharField(max_length=15)
    # ambienteN = models.PositiveIntegerField()
    ambienteT = models.CharField(max_length=70)
    # secaoN = models.PositiveIntegerField()
    secaoT = models.CharField(max_length=70)
    # localN = models.PositiveIntegerField()
    localizacaoT = models.CharField(max_length=70)
    # grupoN = models.PositiveIntegerField()
    grupoT = models.CharField(max_length=70)
    #subGrupoN = models.PositiveIntegerField()
    subGrupoT = models.CharField(max_length=70)
    unidadeMedida = models.ForeignKey(UnidadeMedida, on_delete=models.RESTRICT)
    ambiente = models.ForeignKey(Ambiente, on_delete=models.RESTRICT)
    secao = models.ForeignKey(Secao, on_delete=models.RESTRICT)
    localizacao = models.ForeignKey(Localizacao, on_delete=models.RESTRICT)
    grupo = models.ForeignKey(Grupo, on_delete=models.RESTRICT)
    subgrupo = models.ForeignKey(SubGrupo, on_delete=models.RESTRICT)

    class Meta:
        verbose_name ='Produto'
        verbose_name_plural = 'Produtos'

    def __str__(self):
        return self.descricao
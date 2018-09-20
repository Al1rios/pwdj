from django.db.models import Prefetch, Subquery, OuterRef

from pwdj.galeria.models import Categoria, Model


def buscar_categorias_com_galeria():
    """Busca todas as categorias com os 5 ultimas fotos que foram alteradas

    :return: QuerySet de Categorias
    """
    return Categoria.objects.order_by('titulo').prefetch_related(
        Prefetch(
            'model_set', queryset=Model.objects.filter(
                id__in=Subquery(
                    Model.objects.filter(
                        categoria_id=OuterRef('categoria_id')
                    ).values_list('id', flat=True)[:5]
                )
            ),
            to_attr='galeria'
        )
    )

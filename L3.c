#include <stdio.h>
#include <stdlib.h>

typedef struct no{
    struct no * ant;
    int v;
    struct no * prox;
} no;

struct fila{
    no * inicio;
    no * fim;
    int size;
};

void inicializa(struct fila *f1){
    f1->fim = NULL;
    f1->inicio = NULL;
    f1->size = 0;
}

void insere(struct fila *f, int valor){

    no * novo = (no*) malloc(sizeof(no));
    novo->v = valor;
    no * aux = f->inicio;

    while(valor > aux->v)
        aux = aux->prox;
    novo->ant = aux;
    aux->prox = novo;
    
    f->size++;
}

int deleta(struct fila *f){

    no * aux = f->inicio;
    f->inicio = f->inicio->prox;
    f->inicio->ant = NULL;
    int deletado = aux->v;


    if(aux != NULL)
        free(aux);

    if (f->size > 0)
        f->size--;


    return deletado;
}

void imprimeordem(struct fila *f){

    int qtd = f->size;

    while(qtd--){
        no * aux = f->inicio;

        printf("%d ", aux->v);
        aux = aux->prox;
        deleta(f);
    }

    printf("\n");
}

int main(){
    struct fila f1;
    inicializa(&f1);

    int q, valor;
    scanf("%d", &q);

    while(q--){
        scanf("%d", &valor);
        insere(&f1, valor);
    }

    imprimeordem(&f1);
}

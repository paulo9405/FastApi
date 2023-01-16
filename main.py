from typing import List, Optional
from fastapi import FastAPI
from fastapi import HTTPException, status
from models import Curso


app = FastAPI()

cursos = {
    1: {
        'titulo': 'Programacao para Leigos.',
        'aulas': 112,
        'horas': 58
    },

    2: {
        'titulo': 'Algoritomos e Logica de Programacao.',
        'aulas': 87,
        'horas': 67
    }
    
}


@app.get('/cursos')
async def get_cursos():
    return cursos


@app.get('/cursos/{curso_id}')
async def get_cursos(curso_id: int):
    try:
        curso = cursos[curso_id]
        return curso
    except KeyError:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Curso nao encontrado.')


@app.post('/cursos', status_code=status.HTTP_201_CREATED)
async def post_cursos(curso: Curso):
    next_id: int = len(cursos) + 1
    cursos[next_id] = curso
    del curso.id
    return curso




if __name__ == '__main__':
    import uvicorn

    uvicorn.run('main:app', host='0.0.0.0', port=8000, debug=True, reload=True) 

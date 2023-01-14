from fastapi import FastAPI

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
    curso = cursos[curso_id]
    curso.update({'id': curso_id})
    return curso




if __name__ == '__main__':
    import uvicorn

    uvicorn.run('main:app', host='0.0.0.0', port=8000, debug=True, reload=True) 

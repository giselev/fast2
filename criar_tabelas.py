from core.configs import settings
from core.database import engine
from models.aluno_models import AlunoModel

print('executando documento criar tabelas')
async def create_tables() -> None:
    print('entrando na funcao')

    async with engine.begin() as conn:
        await conn.run_sync(settings.DBBaseModel.metadata.drop_all)
        await conn.run_sync(settings.DBBaseModel.metadata.create_all)
    print('tabela criada com sucesso')

if __name__ == '__main__':
    import asyncio
    asyncio.run(create_tables())
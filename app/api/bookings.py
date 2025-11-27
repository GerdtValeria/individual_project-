from fastapi import APIRouter

router = APIRouter(prefix="/sample",tags=["Sample"])

@router.get("/")
async def get_samples():
    samples = await SampleService().get_all_samples()   
     return samples

@router.get("/{id}")
async def get_sample(id:int):
    sample = await SampleService().get_all_sample(id=id)   
     return sample

@router.post("/")
async def add_sample(sample_data: SSampleAdd):
    await SampleService().add_sample(sample_data)

@router.put("/{id}")
async def edit_sample(id:int, sample_data: SSampleAdd):
    data = await SampleService().edit_sample(id,sample_data)
    return data

@router.delete("/{id}")
async def delete_sample(id:int):
     await SampleService().delete_sample(id=id)   
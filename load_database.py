import pandas as pd
from database.models import Job_1, Job_2, Job_3
import asyncio
from database.database import Session
from sqlalchemy import select
from sentence_transformers import SentenceTransformer
from tqdm import tqdm  # Import tqdm

# Load the model (synchronously)
def load_model(model_name: str):
    model = SentenceTransformer(model_name)
    return model

df = pd.read_csv("Dataset/Job_data_final.csv")
df.dropna(inplace=True)
df = df.astype(str)
# Use a synchronous wrapper for the async insert
async def insert_data_1(model):

    async with Session() as session:
        async with session.begin():
            jobs = []
            
            # Using tqdm to track progress in a synchronous way
            for index, row in tqdm(df.iterrows(), total=len(df), desc="Inserting jobs"):
                try:
                    job_title_vector = model.encode(row['Job Title'])
                    industry_vector = model.encode(row['Industry'])
                    job_skill_vector = model.encode(row['Job Skill'])
                    job_address_vector = model.encode(row['Job Address'])
                    
                    job = Job_1(
                        url=row['URL Job'],
                        job_title=row['Job Title'],
                        company_name=row['Company Name'],
                        industry=row['Industry'],
                        company_address=row['Company Address'],
                        job_description=row['Job Description'],
                        job_requirements=row['Job Requirements'],
                        benefits=row['Benefits'],
                        salary=row['Salary'],
                        expire_date=row['Expire date'],
                        employee_rank=row['Employee Rank'],
                        job_skill=row['Job Skill'],
                        job_field=row['Job Field'],
                        years_of_experience=row['Years of Experience'],
                        job_address=row['Job Address'],
                        job_title_vector=job_title_vector,
                        industry_vector=industry_vector,
                        job_skill_vector=job_skill_vector,
                        job_address_vector=job_address_vector
                    )

                    jobs.append(job)
                except:
                    print("Error in encoding")
                    continue

            # Add all Job_1 objects to the session
            session.add_all(jobs)
            await session.commit()

        print("Inserted Job_1 successfully!")

async def insert_data_2(model):

    async with Session() as session:
        async with session.begin():
            jobs = []
            
            # Using tqdm to track progress in a synchronous way
            for index, row in tqdm(df.iterrows(), total=len(df), desc="Inserting jobs"):
                try:
                    job_title_vector = model.encode(row['Job Title'])
                    industry_vector = model.encode(row['Industry'])
                    job_skill_vector = model.encode(row['Job Skill'])
                    job_address_vector = model.encode(row['Job Address'])
                    
                    job = Job_2(
                        url=row['URL Job'],
                        job_title=row['Job Title'],
                        company_name=row['Company Name'],
                        industry=row['Industry'],
                        company_address=row['Company Address'],
                        job_description=row['Job Description'],
                        job_requirements=row['Job Requirements'],
                        benefits=row['Benefits'],
                        salary=row['Salary'],
                        expire_date=row['Expire date'],
                        employee_rank=row['Employee Rank'],
                        job_skill=row['Job Skill'],
                        job_field=row['Job Field'],
                        years_of_experience=row['Years of Experience'],
                        job_address=row['Job Address'],
                        job_title_vector=job_title_vector,
                        industry_vector=industry_vector,
                        job_skill_vector=job_skill_vector,
                        job_address_vector=job_address_vector
                    )

                    jobs.append(job)
                except:
                    print("Error in encoding")
                    continue

            # Add all Job_1 objects to the session
            session.add_all(jobs)
            await session.commit()

        print("Inserted Job_2 successfully!")


async def insert_data_3(model):

    async with Session() as session:
        async with session.begin():
            jobs = []
            
            # Using tqdm to track progress in a synchronous way
            for index, row in tqdm(df.iterrows(), total=len(df), desc="Inserting jobs"):
                try:
                    job_title_vector = model.encode(row['Job Title'])
                    industry_vector = model.encode(row['Industry'])
                    job_skill_vector = model.encode(row['Job Skill'])
                    job_address_vector = model.encode(row['Job Address'])
                    
                    job = Job_3(
                        url=row['URL Job'],
                        job_title=row['Job Title'],
                        company_name=row['Company Name'],
                        industry=row['Industry'],
                        company_address=row['Company Address'],
                        job_description=row['Job Description'],
                        job_requirements=row['Job Requirements'],
                        benefits=row['Benefits'],
                        salary=row['Salary'],
                        expire_date=row['Expire date'],
                        employee_rank=row['Employee Rank'],
                        job_skill=row['Job Skill'],
                        job_field=row['Job Field'],
                        years_of_experience=row['Years of Experience'],
                        job_address=row['Job Address'],
                        job_title_vector=job_title_vector,
                        industry_vector=industry_vector,
                        job_skill_vector=job_skill_vector,
                        job_address_vector=job_address_vector
                    )

                    jobs.append(job)
                except:
                    print("Error in encoding")
                    continue

            # Add all Job_1 objects to the session
            session.add_all(jobs)
            await session.commit()

        print("Inserted Job_3 successfully!")

# Main function for handling async insert
async def main():
    await insert_data_1(load_model('keepitreal/vietnamese-sbert'))
    await insert_data_2(load_model('vinai/phobert-base'))
    await insert_data_3(load_model('xlm-roberta-base'))


if __name__ == "__main__":
    asyncio.run(main())

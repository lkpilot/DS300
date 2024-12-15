from sqlalchemy import Column, String
from datetime import datetime
from pgvector.sqlalchemy import Vector
from sqlalchemy.dialects.postgresql import UUID
import uuid
from database.database import Base



class Job_1(Base):
    __tablename__ = "jobs_1"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    url = Column(String, nullable=False)
    job_title = Column(String, nullable=False)
    company_name = Column(String, nullable=False)
    industry = Column(String, nullable=False)
    company_address = Column(String, nullable=True)
    job_description = Column(String, nullable=True)
    job_requirements = Column(String, nullable=True)
    benefits = Column(String, nullable=True)
    salary = Column(String, nullable=True)  # Can be changed to a Float if numeric values are standardized
    expire_date = Column(String, nullable=True)  # Can use Date type if date format is standardized
    employee_rank = Column(String, nullable=True)
    job_skill = Column(String, nullable=True)
    job_field = Column(String, nullable=True)
    years_of_experience = Column(String, nullable=True)  # Adjust to Integer if standardized
    job_address = Column(String, nullable=True)


    job_title_vector = Column(Vector(768), nullable=True)
    industry_vector = Column(Vector(768), nullable=True)
    job_skill_vector = Column(Vector(768), nullable=True)
    job_address_vector = Column(Vector(768), nullable=True)

    def __repr__(self):
        return f"<Job(id={self.id}, job_title='{self.job_title}', company_name='{self.company_name}', industry='{self.industry}')>"


class Job_2(Base):
    __tablename__ = "jobs_2"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    url = Column(String, nullable=False)
    job_title = Column(String, nullable=False)
    company_name = Column(String, nullable=False)
    industry = Column(String, nullable=False)
    company_address = Column(String, nullable=True)
    job_description = Column(String, nullable=True)
    job_requirements = Column(String, nullable=True)
    benefits = Column(String, nullable=True)
    salary = Column(String, nullable=True)  # Can be changed to a Float if numeric values are standardized
    expire_date = Column(String, nullable=True)  # Can use Date type if date format is standardized
    employee_rank = Column(String, nullable=True)
    job_skill = Column(String, nullable=True)
    job_field = Column(String, nullable=True)
    years_of_experience = Column(String, nullable=True)  # Adjust to Integer if standardized
    job_address = Column(String, nullable=True)


    job_title_vector = Column(Vector(768), nullable=True)
    industry_vector = Column(Vector(768), nullable=True)
    job_skill_vector = Column(Vector(768), nullable=True)
    job_address_vector = Column(Vector(768), nullable=True)

    def __repr__(self):
        return f"<Job(id={self.id}, job_title='{self.job_title}', company_name='{self.company_name}', industry='{self.industry}')>"
    


class Job_3(Base):
    __tablename__ = "jobs_3"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    url = Column(String, nullable=False)
    job_title = Column(String, nullable=False)
    company_name = Column(String, nullable=False)
    industry = Column(String, nullable=False)
    company_address = Column(String, nullable=True)
    job_description = Column(String, nullable=True)
    job_requirements = Column(String, nullable=True)
    benefits = Column(String, nullable=True)
    salary = Column(String, nullable=True)  # Can be changed to a Float if numeric values are standardized
    expire_date = Column(String, nullable=True)  # Can use Date type if date format is standardized
    employee_rank = Column(String, nullable=True)
    job_skill = Column(String, nullable=True)
    job_field = Column(String, nullable=True)
    years_of_experience = Column(String, nullable=True)  # Adjust to Integer if standardized
    job_address = Column(String, nullable=True)


    job_title_vector = Column(Vector(768), nullable=True)
    industry_vector = Column(Vector(768), nullable=True)
    job_skill_vector = Column(Vector(768), nullable=True)
    job_address_vector = Column(Vector(768), nullable=True)

    def __repr__(self):
        return f"<Job(id={self.id}, job_title='{self.job_title}', company_name='{self.company_name}', industry='{self.industry}')>"
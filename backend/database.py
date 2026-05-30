from sqlalchemy import create_engine

DATABASE_URL = "postgresql://cloudadmin:cloudpassword@192.168.0.145:5432/cloudplatform"

engine = create_engine(DATABASE_URL)

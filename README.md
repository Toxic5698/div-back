# DIVELIT task API Documentation

The DIVELIT task API provides CRUD operations for managing movie records.

## Endpoints

**Docs /docs**
- Returns docs for all endpoints and models

**GET /get-all/**

- Returns a paginated list of movies ordered by descending rating
- Accepts filtering and pagination query parameters

**POST /save/**

- Creates a new movie record
- Accepts a MovieSchemaIn in the request body

**PATCH /update/{id}/**

- Updates a movie by id 
- Accepts a MovieSchemaIn in the request body
- Returns 404 if not found

**DELETE /delete/{id}/**

- Deletes a movie by id
- Returns 404 if not found

**GET /stats/**

- Returns overall statistics about movie ratings
  - Total number of movies
  - Highest rating
  - Lowest rating
  - Median rating
  
## Models

**Movie**

- id: Integer primary key
- name: String name of movie
- rate: Integer rating of movie
- added_at: DateTime movie was added

## Schemas 

**MovieSchemaIn**

- name: String
- rate: Integer

**MovieSchemaOut** 

- id: Integer  
- added_at: DateTime
- name: String
- rate: Integer


Live demo available on: https://div-back.vercel.app/docs

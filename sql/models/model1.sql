WITH input AS (

  SELECT * 
  
  FROM {{ ref('input')}}

),

deduplicate_1 AS (

  {#Removes duplicate entries from a dataset to ensure data integrity.#}
  {{ sql_gem_examples.deduplicate('input', 'id', 'id') }}

),

deduplicated_names AS (

  {#Removes duplicate entries based on first and last names for cleaner data management.#}
  {{ sql_gem_examples.deduplicate('input', 'first_name', 'last_name') }}

)

SELECT *

FROM deduplicate_1

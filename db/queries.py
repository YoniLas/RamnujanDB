GET_CONSTANTS = "SELECT * FROM constant"
ADD_CONSTANT = "INSERT INTO constant ({columns}) VALUES ({values}) RETURNING constant_id"
ADD_CF = "INSERT INTO Cf ({columns}) VALUES ({values}) RETURNING cf_id" 
UPDATE_CF_PRECISION = "UPDATE Cf SET precision = (something) WHERE cf_id = (something else)"

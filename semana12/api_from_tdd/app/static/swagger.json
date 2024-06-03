{
    "openapi": "3.0.1",
    "info": {
        "title": "Tienda Online API",
        "version": "1.0.0"
    },
    "paths": {
        "/api/products": {
            "get": {
                "summary": "Obtiene la lista de todos los productos",
                "security": [
                    {
                        "JWTAuth": []
                    }
                ],
                "responses": {
                    "200": {
                        "description": "Lista de productos",
                        "content": {
                            "application/json": {
                                "schema": {
                                    "type": "array",
                                    "items": {
                                        "$ref": "#/components/schemas/Product"
                                    }
                                }
                            }
                        }
                    }
                }
            },
            "post": {
                "summary": "Crea un nuevo producto",
                "security": [
                    {
                        "JWTAuth": []
                    }
                ],
                "requestBody": {
                    "content": {
                        "application/json": {
                            "schema": {
                                "$ref": "#/components/schemas/Product"
                            }
                        }
                    }
                },
                "responses": {
                    "201": {
                        "description": "Producto creado",
                        "content": {
                            "application/json": {
                                "schema": {
                                    "$ref": "#/components/schemas/Product"
                                }
                            }
                        }
                    }
                }
            }
        },
        "/api/products/{id}": {
            "get": {
                "summary": "Obtiene un producto específico por su ID",
                "security": [
                    {
                        "JWTAuth": []
                    }
                ],
                "parameters": [
                    {
                        "name": "id",
                        "in": "path",
                        "required": true,
                        "schema": {
                            "type": "integer"
                        }
                    }
                ],
                "responses": {
                    "200": {
                        "description": "Detalles del producto",
                        "content": {
                            "application/json": {
                                "schema": {
                                    "$ref": "#/components/schemas/Product"
                                }
                            }
                        }
                    },
                    "404": {
                        "description": "Producto no encontrado"
                    }
                }
            },
            "put": {
                "summary": "Actualiza un producto existente por su ID",
                "security": [
                    {
                        "JWTAuth": []
                    }
                ],
                "parameters": [
                    {
                        "name": "id",
                        "in": "path",
                        "required": true,
                        "schema": {
                            "type": "integer"
                        }
                    }
                ],
                "requestBody": {
                    "content": {
                        "application/json": {
                            "schema": {
                                "$ref": "#/components/schemas/Product"
                            }
                        }
                    }
                },
                "responses": {
                    "200": {
                        "description": "Producto actualizado",
                        "content": {
                            "application/json": {
                                "schema": {
                                    "$ref": "#/components/schemas/Product"
                                }
                            }
                        }
                    },
                    "404": {
                        "description": "Producto no encontrado"
                    }
                }
            },
            "delete": {
                "summary": "Elimina un producto existente por su ID",
                "security": [
                    {
                        "JWTAuth": []
                    }
                ],
                "parameters": [
                    {
                        "name": "id",
                        "in": "path",
                        "required": true,
                        "schema": {
                            "type": "integer"
                        }
                    }
                ],
                "responses": {
                    "204": {
                        "description": "Producto eliminado"
                    },
                    "404": {
                        "description": "Producto no encontrado"
                    }
                }
            }
        },
        "/api/register": {
            "post": {
                "summary": "Registra un nuevo usuario",
                "requestBody": {
                    "content": {
                        "application/json": {
                            "schema": {
                                "$ref": "#/components/schemas/User"
                            }
                        }
                    }
                },
                "responses": {
                    "201": {
                        "description": "Usuario creado"
                    },
                    "400": {
                        "description": "Solicitud incorrecta"
                    }
                }
            }
        },
        "/api/login": {
            "post": {
                "summary": "Inicia sesión con un usuario existente",
                "requestBody": {
                    "content": {
                        "application/json": {
                            "schema": {
                                "$ref": "#/components/schemas/Login"
                            }
                        }
                    }
                },
                "responses": {
                    "200": {
                        "description": "Inicio de sesión exitoso",
                        "content": {
                            "application/json": {
                                "schema": {
                                    "$ref": "#/components/schemas/Token"
                                }
                            }
                        }
                    },
                    "401": {
                        "description": "Credenciales inválidas"
                    }
                }
            }
        }
    },
    "components": {
        "securitySchemes": {
            "JWTAuth": {
                "type": "http",
                "scheme": "bearer",
                "bearerFormat": "JWT"
            }
        },
        "schemas": {
            "Product": {
                "type": "object",
                "properties": {
                    "id": {
                        "type": "integer",
                        "readOnly": true
                    },
                    "name": {
                        "type": "string"
                    },
                    "description": {
                        "type": "string"
                    },
                    "price": {
                        "type": "number",
                        "format": "float"
                    },
                    "stock": {
                        "type": "integer"
                    }
                },
                "required": [
                    "name",
                    "description",
                    "price",
                    "stock"
                ]
            },
            "User": {
                "type": "object",
                "properties": {
                    "username": {
                        "type": "string"
                    },
                    "password": {
                        "type": "string"
                    },
                    "roles": {
                        "type": "array",
                        "items": {
                            "type": "string",
                            "enum": [
                                "admin",
                                "user"
                            ]
                        }
                    }
                },
                "required": [
                    "username",
                    "password",
                    "roles"
                ]
            },
            "Login": {
                "type": "object",
                "properties": {
                    "username": {
                        "type": "string"
                    },
                    "password": {
                        "type": "string"
                    }
                },
                "required": [
                    "username",
                    "password"
                ]
            }
        }
    }
}
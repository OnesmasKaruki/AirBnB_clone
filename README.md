# AirBnb clone
The goal of the project is to deploy on your server a simple copy of the AirBnb website. Which is bisically a clone of AirBnb.
We eon,t implement all the features, only some of them to cover all the fundamental concepts of higer level programming track.

## Complete web application composed by:
* A command interpreter to manupulate and control data withoout a visual interface, like in Shell(Perfect development and debugging).
* A website(FFRONT-END) that shows the final product to everyone: static and dynamic
* A database or file that can store data/Object.
* An API that provides a communication interface  between the front-end and database (retreive, create, delete, update them)

### Files and Dictonaries

* repr(models) directory will contain all classes used for the entire project. Aclass, called "model" in OOP prooject is the representation of an obl=ject/instance and used during manipulation
* repr(tests) directory will contain all unit tests of all code coverage.
* repr(console.py) file is the entry ppoint of our command interpreter.
* repr(models/base_model.py) file is the base class of all our models, It contains common element
    * attributes: repr(id, created_at) and repr(update_at)
    * methods: repr(save()) and repr(to_json())
* repr(models/engine) directory will contain all storrage class (using the same prototype). For the moment you will have only one repr(file_storage.py)

/* Copyright (c) 2005 - 2015 Hewlett Packard Enterprise Development LP -*- C++ -*- */
/* 
 * Description: Example User Defined Aggregate Function: Average
 *
 */

#include "Vertica.h"
#include <time.h> 
#include <sstream>
#include <iostream>

using namespace Vertica;
using namespace std;



/****
 * Example implementation of Average: intermediate is a 2 part type: running
 * sum and count.
 ***/
class Multiply : public AggregateFunction
{
    virtual void initAggregate(ServerInterface &srvInterface, 
                       IntermediateAggs &aggs)
    {
        
            vfloat &product = aggs.getFloatRef(0);
            product = 1;
     
        
    }
    
    void aggregate(ServerInterface &srvInterface, 
                   BlockReader &argReader, 
                   IntermediateAggs &aggs)
    {
        
            vfloat &product = aggs.getFloatRef(0);
            

            do {
                const vfloat &input = argReader.getFloatRef(0);
                product = input*product;
                
                
            } while (argReader.next());
        
    }

    virtual void combine(ServerInterface &srvInterface, 
                         IntermediateAggs &aggs, 
                         MultipleIntermediateAggs &aggsOther)
    {
        
            vfloat       &myProduct      = aggs.getFloatRef(0);
            // Combine all the other intermediate aggregates
            do {
                const vfloat &otherProduct   = aggsOther.getFloatRef(0);
                            
                // Do the actual accumulation 
                myProduct = myProduct*otherProduct;
                
            } while (aggsOther.next());
        
    }

    virtual void terminate(ServerInterface &srvInterface, 
                           BlockWriter &resWriter, 
                           IntermediateAggs &aggs)
    {
            // Metadata about the type (to allow creation)
            
            const vfloat     &product     = aggs.getFloatRef(0);

            //vfloat &out = resWriter.setFloat();
            
            //out = product;
            resWriter.setFloat(product);
        
    }

    InlineAggregate()
};


/*
 * This class provides the meta-data associated with the aggregate function
 * shown above, as well as a way of instantiating objects of the class. 
 */
class MultiplyFactory : public AggregateFunctionFactory
{
    virtual void getPrototype(ServerInterface &srvfloaterface, 
                              ColumnTypes &argTypes, 
                              ColumnTypes &returnType)
    {
        argTypes.addFloat();
        returnType.addFloat();
    }

    // Provide return type length/scale/precision information (given the input
    // type length/scale/precision), as well as column names
    virtual void getReturnType(ServerInterface &srvfloaterface, 
                               const SizedColumnTypes &inputTypes, 
                               SizedColumnTypes &outputTypes)
    {
        //int int_part = inputTypes.getColumnType(0).getNumericPrecision();
        //int frac_part = inputTypes.getColumnType(0).getNumericScale();
        //outputTypes.addNumeric(int_part+frac_part, frac_part);
        outputTypes.addFloat();
    }

    virtual void getIntermediateTypes(ServerInterface &srvInterface,
                                      const SizedColumnTypes &inputTypes, 
                                      SizedColumnTypes 
                                      &intermediateTypeMetaData)
    {
        
        intermediateTypeMetaData.addFloat();
    }

    // Create an instance of the AggregateFunction
    virtual AggregateFunction *createAggregateFunction(ServerInterface &srvfloaterface)
    { return vt_createFuncObject<Multiply>(srvfloaterface.allocator); }

};

RegisterFactory(MultiplyFactory);


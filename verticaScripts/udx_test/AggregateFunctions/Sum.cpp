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
class Sum : public AggregateFunction
{
    virtual void initAggregate(ServerInterface &srvInterface, 
                       IntermediateAggs &aggs)
    {
            vfloat &sum = aggs.getFloatRef(0);
            sum = 0;
                 
    }
    
    void aggregate(ServerInterface &srvInterface, 
                   BlockReader &argReader, 
                   IntermediateAggs &aggs)
    {
       
            vfloat &sum = aggs.getFloatRef(0);
            do {
                const vfloat &input = argReader.getFloatRef(0);
                sum += input;
                    
                } while (argReader.next());
        
    }

    virtual void combine(ServerInterface &srvInterface, 
                         IntermediateAggs &aggs, 
                         MultipleIntermediateAggs &aggsOther)
    {
        
            vfloat       &mySum      = aggs.getFloatRef(0);

            // Combine all the other intermediate aggregates
            do {
                const vfloat &otherSum   = aggsOther.getFloatRef(0);
                
            
                // Do the actual accumulation 
                mySum += otherSum;
                

            } while (aggsOther.next());
        
    }

    virtual void terminate(ServerInterface &srvInterface, 
                           BlockWriter &resWriter, 
                           IntermediateAggs &aggs)
    {
             // Metadata about the type (to allow creation)
            
            const vfloat     &sum     = aggs.getFloatRef(0);

            // Get the count as a numeric by making a local numeric
            //uint64 tmp[sum.getMaxSize() / sizeof(uint64)];
            
            resWriter.setFloat(sum);
            
    }

    InlineAggregate()
};


/*
 * This class provides the meta-data associated with the aggregate function
 * shown above, as well as a way of instantiating objects of the class. 
 */
class SumFactory : public AggregateFunctionFactory
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
        
        outputTypes.addFloat();
    }

    virtual void getIntermediateTypes(ServerInterface &srvInterface,
                                      const SizedColumnTypes &inputTypes, 
                                      SizedColumnTypes 
                                      &intermediateTypeMetaData)
    {
            intermediateTypeMetaData.addFloat(); // intermediate sum
        
    }

    // Create an instance of the AggregateFunction
    virtual AggregateFunction *createAggregateFunction(ServerInterface &srvfloaterface)
    { return vt_createFuncObject<Sum>(srvfloaterface.allocator); }

};

RegisterFactory(SumFactory);


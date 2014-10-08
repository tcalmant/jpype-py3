/*****************************************************************************
   Copyright 2004 Steve Ménard

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.
   
*****************************************************************************/   
#ifndef _JPARRAY_H_
#define _JPARRAY_H_

/**
 * Class to wrap Java Class and provide low-level behavior
 */
class JPArray : public JPObjectBase
{
public :
	JPArray(JPTypeName name, jarray inst);
	virtual~ JPArray();

public :
	JPArrayClass* getClass()
	{
		return m_Class;
	}

	int       getLength();	
	vector<HostRef*>  getRange(int start, int stop);
	void      setRange(int start, int stop, vector<HostRef*>& val);
	void      setItem(int ndx, HostRef*);
	HostRef*  getItem(int ndx);

	void      setContent(vector<HostRef*>& data)
	{
		setRange(0, getLength(), data);  
	}

	jobject getObject()
	{
		return JPEnv::getJava()->NewLocalRef(m_Object);
	}

public : // Wrapper
	virtual JPType* getType();
	virtual jvalue  getValue();
	virtual JCharString toString();

private :
	JPArrayClass* m_Class;
	jarray	      m_Object;
};


#endif // _JPARRAY_H_
/* 
  Cuda Templates.

  Copyright (C) 2008 Institute for Computer Graphics and Vision,
                     Graz University of Technology
  
  This program is free software; you can redistribute it and/or modify
  it under the terms of the GNU General Public License as published by
  the Free Software Foundation; either version 3 of the License, or
  (at your option) any later version.
  
  This program is distributed in the hope that it will be useful,
  but WITHOUT ANY WARRANTY; without even the implied warranty of
  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
  GNU General Public License for more details.
  
  You should have received a copy of the GNU General Public License
  along with this program.  If not, see <http://www.gnu.org/licenses/>.
*/

#ifndef CUDA_DEVICEPROPERTIES_H
#define CUDA_DEVICEPROPERTIES_H


#include <cutil.h>

#include <cudatemplates/error.hpp>


/**
   This namespace contains all classes and functions of the CUDA templates.
*/
namespace Cuda {

/**
   Properties of CUDA device.
*/
class DeviceProperties: public cudaDeviceProp
{
public:
  /**
     Constructor.
     @param dev device number
  */
  inline DeviceProperties(int dev = -1)
  {
    if(dev < 0)
      CUDA_CHECK(cudaGetDevice(&dev));

    cudaGetDeviceProperties(this, dev);
    CUDA_CHECK_LAST;
  }
};

}  // namespace Cuda


#endif

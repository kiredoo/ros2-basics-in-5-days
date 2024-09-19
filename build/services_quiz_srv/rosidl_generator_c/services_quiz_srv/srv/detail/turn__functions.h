// generated from rosidl_generator_c/resource/idl__functions.h.em
// with input from services_quiz_srv:srv/Turn.idl
// generated code does not contain a copyright notice

#ifndef SERVICES_QUIZ_SRV__SRV__DETAIL__TURN__FUNCTIONS_H_
#define SERVICES_QUIZ_SRV__SRV__DETAIL__TURN__FUNCTIONS_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stdlib.h>

#include "rosidl_runtime_c/visibility_control.h"
#include "services_quiz_srv/msg/rosidl_generator_c__visibility_control.h"

#include "services_quiz_srv/srv/detail/turn__struct.h"

/// Initialize srv/Turn message.
/**
 * If the init function is called twice for the same message without
 * calling fini inbetween previously allocated memory will be leaked.
 * \param[in,out] msg The previously allocated message pointer.
 * Fields without a default value will not be initialized by this function.
 * You might want to call memset(msg, 0, sizeof(
 * services_quiz_srv__srv__Turn_Request
 * )) before or use
 * services_quiz_srv__srv__Turn_Request__create()
 * to allocate and initialize the message.
 * \return true if initialization was successful, otherwise false
 */
ROSIDL_GENERATOR_C_PUBLIC_services_quiz_srv
bool
services_quiz_srv__srv__Turn_Request__init(services_quiz_srv__srv__Turn_Request * msg);

/// Finalize srv/Turn message.
/**
 * \param[in,out] msg The allocated message pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_services_quiz_srv
void
services_quiz_srv__srv__Turn_Request__fini(services_quiz_srv__srv__Turn_Request * msg);

/// Create srv/Turn message.
/**
 * It allocates the memory for the message, sets the memory to zero, and
 * calls
 * services_quiz_srv__srv__Turn_Request__init().
 * \return The pointer to the initialized message if successful,
 * otherwise NULL
 */
ROSIDL_GENERATOR_C_PUBLIC_services_quiz_srv
services_quiz_srv__srv__Turn_Request *
services_quiz_srv__srv__Turn_Request__create();

/// Destroy srv/Turn message.
/**
 * It calls
 * services_quiz_srv__srv__Turn_Request__fini()
 * and frees the memory of the message.
 * \param[in,out] msg The allocated message pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_services_quiz_srv
void
services_quiz_srv__srv__Turn_Request__destroy(services_quiz_srv__srv__Turn_Request * msg);

/// Check for srv/Turn message equality.
/**
 * \param[in] lhs The message on the left hand size of the equality operator.
 * \param[in] rhs The message on the right hand size of the equality operator.
 * \return true if messages are equal, otherwise false.
 */
ROSIDL_GENERATOR_C_PUBLIC_services_quiz_srv
bool
services_quiz_srv__srv__Turn_Request__are_equal(const services_quiz_srv__srv__Turn_Request * lhs, const services_quiz_srv__srv__Turn_Request * rhs);

/// Copy a srv/Turn message.
/**
 * This functions performs a deep copy, as opposed to the shallow copy that
 * plain assignment yields.
 *
 * \param[in] input The source message pointer.
 * \param[out] output The target message pointer, which must
 *   have been initialized before calling this function.
 * \return true if successful, or false if either pointer is null
 *   or memory allocation fails.
 */
ROSIDL_GENERATOR_C_PUBLIC_services_quiz_srv
bool
services_quiz_srv__srv__Turn_Request__copy(
  const services_quiz_srv__srv__Turn_Request * input,
  services_quiz_srv__srv__Turn_Request * output);

/// Initialize array of srv/Turn messages.
/**
 * It allocates the memory for the number of elements and calls
 * services_quiz_srv__srv__Turn_Request__init()
 * for each element of the array.
 * \param[in,out] array The allocated array pointer.
 * \param[in] size The size / capacity of the array.
 * \return true if initialization was successful, otherwise false
 * If the array pointer is valid and the size is zero it is guaranteed
 # to return true.
 */
ROSIDL_GENERATOR_C_PUBLIC_services_quiz_srv
bool
services_quiz_srv__srv__Turn_Request__Sequence__init(services_quiz_srv__srv__Turn_Request__Sequence * array, size_t size);

/// Finalize array of srv/Turn messages.
/**
 * It calls
 * services_quiz_srv__srv__Turn_Request__fini()
 * for each element of the array and frees the memory for the number of
 * elements.
 * \param[in,out] array The initialized array pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_services_quiz_srv
void
services_quiz_srv__srv__Turn_Request__Sequence__fini(services_quiz_srv__srv__Turn_Request__Sequence * array);

/// Create array of srv/Turn messages.
/**
 * It allocates the memory for the array and calls
 * services_quiz_srv__srv__Turn_Request__Sequence__init().
 * \param[in] size The size / capacity of the array.
 * \return The pointer to the initialized array if successful, otherwise NULL
 */
ROSIDL_GENERATOR_C_PUBLIC_services_quiz_srv
services_quiz_srv__srv__Turn_Request__Sequence *
services_quiz_srv__srv__Turn_Request__Sequence__create(size_t size);

/// Destroy array of srv/Turn messages.
/**
 * It calls
 * services_quiz_srv__srv__Turn_Request__Sequence__fini()
 * on the array,
 * and frees the memory of the array.
 * \param[in,out] array The initialized array pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_services_quiz_srv
void
services_quiz_srv__srv__Turn_Request__Sequence__destroy(services_quiz_srv__srv__Turn_Request__Sequence * array);

/// Check for srv/Turn message array equality.
/**
 * \param[in] lhs The message array on the left hand size of the equality operator.
 * \param[in] rhs The message array on the right hand size of the equality operator.
 * \return true if message arrays are equal in size and content, otherwise false.
 */
ROSIDL_GENERATOR_C_PUBLIC_services_quiz_srv
bool
services_quiz_srv__srv__Turn_Request__Sequence__are_equal(const services_quiz_srv__srv__Turn_Request__Sequence * lhs, const services_quiz_srv__srv__Turn_Request__Sequence * rhs);

/// Copy an array of srv/Turn messages.
/**
 * This functions performs a deep copy, as opposed to the shallow copy that
 * plain assignment yields.
 *
 * \param[in] input The source array pointer.
 * \param[out] output The target array pointer, which must
 *   have been initialized before calling this function.
 * \return true if successful, or false if either pointer
 *   is null or memory allocation fails.
 */
ROSIDL_GENERATOR_C_PUBLIC_services_quiz_srv
bool
services_quiz_srv__srv__Turn_Request__Sequence__copy(
  const services_quiz_srv__srv__Turn_Request__Sequence * input,
  services_quiz_srv__srv__Turn_Request__Sequence * output);

/// Initialize srv/Turn message.
/**
 * If the init function is called twice for the same message without
 * calling fini inbetween previously allocated memory will be leaked.
 * \param[in,out] msg The previously allocated message pointer.
 * Fields without a default value will not be initialized by this function.
 * You might want to call memset(msg, 0, sizeof(
 * services_quiz_srv__srv__Turn_Response
 * )) before or use
 * services_quiz_srv__srv__Turn_Response__create()
 * to allocate and initialize the message.
 * \return true if initialization was successful, otherwise false
 */
ROSIDL_GENERATOR_C_PUBLIC_services_quiz_srv
bool
services_quiz_srv__srv__Turn_Response__init(services_quiz_srv__srv__Turn_Response * msg);

/// Finalize srv/Turn message.
/**
 * \param[in,out] msg The allocated message pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_services_quiz_srv
void
services_quiz_srv__srv__Turn_Response__fini(services_quiz_srv__srv__Turn_Response * msg);

/// Create srv/Turn message.
/**
 * It allocates the memory for the message, sets the memory to zero, and
 * calls
 * services_quiz_srv__srv__Turn_Response__init().
 * \return The pointer to the initialized message if successful,
 * otherwise NULL
 */
ROSIDL_GENERATOR_C_PUBLIC_services_quiz_srv
services_quiz_srv__srv__Turn_Response *
services_quiz_srv__srv__Turn_Response__create();

/// Destroy srv/Turn message.
/**
 * It calls
 * services_quiz_srv__srv__Turn_Response__fini()
 * and frees the memory of the message.
 * \param[in,out] msg The allocated message pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_services_quiz_srv
void
services_quiz_srv__srv__Turn_Response__destroy(services_quiz_srv__srv__Turn_Response * msg);

/// Check for srv/Turn message equality.
/**
 * \param[in] lhs The message on the left hand size of the equality operator.
 * \param[in] rhs The message on the right hand size of the equality operator.
 * \return true if messages are equal, otherwise false.
 */
ROSIDL_GENERATOR_C_PUBLIC_services_quiz_srv
bool
services_quiz_srv__srv__Turn_Response__are_equal(const services_quiz_srv__srv__Turn_Response * lhs, const services_quiz_srv__srv__Turn_Response * rhs);

/// Copy a srv/Turn message.
/**
 * This functions performs a deep copy, as opposed to the shallow copy that
 * plain assignment yields.
 *
 * \param[in] input The source message pointer.
 * \param[out] output The target message pointer, which must
 *   have been initialized before calling this function.
 * \return true if successful, or false if either pointer is null
 *   or memory allocation fails.
 */
ROSIDL_GENERATOR_C_PUBLIC_services_quiz_srv
bool
services_quiz_srv__srv__Turn_Response__copy(
  const services_quiz_srv__srv__Turn_Response * input,
  services_quiz_srv__srv__Turn_Response * output);

/// Initialize array of srv/Turn messages.
/**
 * It allocates the memory for the number of elements and calls
 * services_quiz_srv__srv__Turn_Response__init()
 * for each element of the array.
 * \param[in,out] array The allocated array pointer.
 * \param[in] size The size / capacity of the array.
 * \return true if initialization was successful, otherwise false
 * If the array pointer is valid and the size is zero it is guaranteed
 # to return true.
 */
ROSIDL_GENERATOR_C_PUBLIC_services_quiz_srv
bool
services_quiz_srv__srv__Turn_Response__Sequence__init(services_quiz_srv__srv__Turn_Response__Sequence * array, size_t size);

/// Finalize array of srv/Turn messages.
/**
 * It calls
 * services_quiz_srv__srv__Turn_Response__fini()
 * for each element of the array and frees the memory for the number of
 * elements.
 * \param[in,out] array The initialized array pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_services_quiz_srv
void
services_quiz_srv__srv__Turn_Response__Sequence__fini(services_quiz_srv__srv__Turn_Response__Sequence * array);

/// Create array of srv/Turn messages.
/**
 * It allocates the memory for the array and calls
 * services_quiz_srv__srv__Turn_Response__Sequence__init().
 * \param[in] size The size / capacity of the array.
 * \return The pointer to the initialized array if successful, otherwise NULL
 */
ROSIDL_GENERATOR_C_PUBLIC_services_quiz_srv
services_quiz_srv__srv__Turn_Response__Sequence *
services_quiz_srv__srv__Turn_Response__Sequence__create(size_t size);

/// Destroy array of srv/Turn messages.
/**
 * It calls
 * services_quiz_srv__srv__Turn_Response__Sequence__fini()
 * on the array,
 * and frees the memory of the array.
 * \param[in,out] array The initialized array pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_services_quiz_srv
void
services_quiz_srv__srv__Turn_Response__Sequence__destroy(services_quiz_srv__srv__Turn_Response__Sequence * array);

/// Check for srv/Turn message array equality.
/**
 * \param[in] lhs The message array on the left hand size of the equality operator.
 * \param[in] rhs The message array on the right hand size of the equality operator.
 * \return true if message arrays are equal in size and content, otherwise false.
 */
ROSIDL_GENERATOR_C_PUBLIC_services_quiz_srv
bool
services_quiz_srv__srv__Turn_Response__Sequence__are_equal(const services_quiz_srv__srv__Turn_Response__Sequence * lhs, const services_quiz_srv__srv__Turn_Response__Sequence * rhs);

/// Copy an array of srv/Turn messages.
/**
 * This functions performs a deep copy, as opposed to the shallow copy that
 * plain assignment yields.
 *
 * \param[in] input The source array pointer.
 * \param[out] output The target array pointer, which must
 *   have been initialized before calling this function.
 * \return true if successful, or false if either pointer
 *   is null or memory allocation fails.
 */
ROSIDL_GENERATOR_C_PUBLIC_services_quiz_srv
bool
services_quiz_srv__srv__Turn_Response__Sequence__copy(
  const services_quiz_srv__srv__Turn_Response__Sequence * input,
  services_quiz_srv__srv__Turn_Response__Sequence * output);

#ifdef __cplusplus
}
#endif

#endif  // SERVICES_QUIZ_SRV__SRV__DETAIL__TURN__FUNCTIONS_H_

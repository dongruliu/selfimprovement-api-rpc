namespace py example

struct MyStruct {
  1: i32 field1,
  2: string field2,
}

service MyService {
  i32 add(1:i32 arg1, 2:i32 arg2),
  string concatenate(1:string s1, 2:string s2),
}

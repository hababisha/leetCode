use std::collections::HashMap;

impl Solution {
    pub fn is_anagram(s: String, t: String) -> bool {
        let mut m1 = HashMap::<char, i32>::new();
        let mut m2 = HashMap::<char, i32>::new();

        let s1 = s.chars().into_iter();
        let t2 = t.chars().into_iter();

        for i in s1{
            if m1.contains_key(&i){
                m1.insert(i, m1.get(&i).unwrap()+1);
            }else{
                m1.insert(i, 1);
            }
        }

        for i in t2{
            if m2.contains_key(&i){
                m2.insert(i,m2.get(&i).unwrap()+1);
            }else{
                m2.insert(i, 1);
            }
        }

        return m1 == m2;
    }
}
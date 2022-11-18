#!/usr/bin/env python3
# coding:utf-8
WF = {
    "Q1": "MATCH (p:Pangenome)<-[:IS_IN_PANGENOME]-(f:Family) "
          "WHERE f.annotation IS NOT NULL "
          "RETURN p.name, count(f)",
    "Q2": "MATCH (p:Pangenome)<-[:IS_IN_PANGENOME]-(f:Family) "
          "WHERE f.annotation IS NOT NULL "
          "RETURN p.name, count(f)",
    "Q3": "MATCH (p:Pangenome)<-[:IS_IN_PANGENOME]-(f:Family)<-[:IS_IN_FAMILY]-(:Gene)-[:IS_IN_RGP]->(r:RGP)-[:IS_IN_SPOT]-(s:Spot) "
          "WHERE f.annotation IS NOT NULL "
          "WITH f, p, s, count(DISTINCT r) AS cnt ORDER BY cnt DESC "
          "RETURN f.name, p.name, cnt, s.name",
    "Q4": "MATCH (p:Pangenome)<-[:IS_IN_PANGENOME]-(f:Family)<-[:IS_IN_FAMILY]-(g:Gene)-[:IS_IN_RGP]->(r:RGP) "
          "WITH p, count(DISTINCT r) AS cnt ORDER BY cnt DESC LIMIT 10 "
          "RETURN p.name, cnt",
    "Q5": "MATCH (p:Pangenome)<-[:IS_IN_PANGENOME]-(f:Family)-[:IS_IN_MODULE]->(m:Module) "
          "WITH p, count(DISTINCT f) AS cnt ORDER BY cnt DESC LIMIT 10 "
          "RETURN p.name, cnt",
    "Q6": "MATCH (p:Pangenome)<-[:IS_IN_PANGENOME]-(f:Family)-[:IS_IN_MODULE]->(m:Module) "
          "WITH p, count(DISTINCT m) AS cnt ORDER BY cnt DESC LIMIT 10 "
          "RETURN p.name, cnt",
    "Q7": "MATCH (p1:Pangenome)<-[:IS_IN_PANGENOME]-(f1:Family)-[:HAS_PARTITION]->(s1:Partition) "
          "WITH p1, f1, s1 MATCH (f1)-[IS_SIMILAR]-(f2:Family) -[:HAS_PARTITION]->(s2) "
          "WITH p1, f1, s1, s2, f2 "
          "MATCH (p2:Pangenome)<-[IS_IN_PANGENOME]-(f2) "
          "WHERE p1.name <> p2.name "
          "RETURN p1.name, f1.name, s1.partition, p2.name, f2.name, s2.partition",
    "Q8": "MATCH a=(p:Partition)<-[HAS_PARTITION]-(f1:Family) -[:IS_IN_FAMILY]-(g:Gene)-[:IS_IN_RGP]-(r:RGP)-[:IS_IN_SPOT]-(s:Spot) "
          "WITH a,p,f1,g,r,s "
          "MATCH b=(z1:Pangenome)-[:IS_IN_PANGENOME]-(f1)-[:IS_SIMILAR]-(f2:Family)-[:IS_IN_PANGENOME]-(z2:Pangenome) "
          "WHERE f1.annotation IS NOT NULL AND z1<>z2 "
          "WITH a,b,p,f1,g,r,s,z1,z2,f2 "
          "MATCH c=(f2)-[:HAS_PARTITION]-(p2)"
          "RETURN a,b,c",
    "Q9": "MATCH (m1:Module)<-[:IS_IN_MODULE]-(f1:Family)-[:IS_IN_PANGENOME]->(p1:Pangenome) "
          "WITH f1, m1, p1 MATCH (p2:Pangenome)<-[:IS_IN_PANGENOME]-(f2:Family)-[:IS_SIMILAR]-(f1) "
          "WITH f1, m1, p1, f2, p2 MATCH (f2)-[:IS_IN_MODULE]-(m2:Module) "
          "WHERE f1.annotation IS NOT NULL AND p1 <> p2 "
          "RETURN p1, p2, m1, m2, f1, f2",
    "Q10": "MATCH (f1:Family)-[:HAS_PARTITION]->(s1:Partition) "
           "WITH f1, s1 MATCH (f1)-[r1:IS_SIMILAR]->(f2) -[:HAS_PARTITION]->(s2:Partition) "
           "WHERE r1.identity >= 0.8 AND r1.coverage >= 0.8 "
           "RETURN f1.name, s1.partition, f2.name, s2.partition, r1.identity, r1.coverage,f1.annotation, f2.annotation "
           "ORDER BY r1.identity LIMIT 10"
}

# start
N, M, V = map( int, input().split() )
edge = [ set() for i in range( N+1 ) ]

for i in range( M ) :
    a, b = map( int, input().split() )
    edge[a].add( b )
    edge[b].add( a )

# DFS
visited = set()
Q = [ V ]
while Q :
    q = Q.pop( -1 )

    if q in visited :
        continue
    else :
        pass

    print( q, end = ' ' )
    visited.add( q )

    for next in sorted( edge[q], reverse = True ) :
        Q.append( next )

print()

# BFS
visited = set()
Q = [ V ]
while Q :
    q = Q.pop( 0 )

    if q in visited :
        continue
    else :
        pass

    print( q, end = ' ' )
    visited.add( q )

    for next in sorted( edge[q] ) :
        Q.append( next )

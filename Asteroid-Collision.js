/**
 * @param {number[]} asteroids
 * @return {number[]}
 */
// Utilizing a stack, only adding the survivied remain asteroids after collision.
//  We iterate over asteroids once (for loop).
// Collisions happen inside the while loop, which runs only when necessary:
// Asteroids moving in opposite directions (>0 vs <0) collide.
// The larger asteroid survives, and the smaller gets removed.
// If equal in size, both are destroyed.
// Only the surviving asteroid is pushed into the stack.
// example 4: [-1, 1, -2, 2] -> [-1, -2, 2] -1 and 1 are actually moving away from each other
// example 5: [1, 2, 3, 4, 5, -6] -> [-6] O(2n) -> O(n)
var asteroidCollision = function(asteroids) {
    let stack = [];
    
    for (let asteroid of asteroids) {
        while (
            //while we have a collision: stack is not empty && The current asteroid is moving left(<0). && the last asteroid in the stack is moving right (>0)
            stack.length && asteroid < 0 && stack[stack.length-1] > 0
        ) {
            let top = stack.pop(); // Remove the last right-moving asteroid
            
            if (Math.abs(top) > Math.abs(asteroid)) {
                stack.push(top); // Top asteroid survives, re-add it
                asteroid = 0; // Mark asteroid as destroyed
            } else if (Math.abs(top) === Math.abs(asteroid)) {
                asteroid = 0; // Both asteroids destroy each other
            }
        }
        
        if (asteroid) stack.push(asteroid); // Add only if not destroyed
    }
    
    return stack;
};

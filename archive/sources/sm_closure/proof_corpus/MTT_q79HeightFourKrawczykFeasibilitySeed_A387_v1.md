# MTT q79 Height-Four Krawczyk Feasibility Seed (A387) v1

A387 combines the tightened A386 value enclosure with the certified A384 point Jacobian. It separates the floating Newton seed from the midpoint of the much wider rigorous residual box and executes a componentwise positive Krawczyk scale diagnostic.

The independent floating residual norm is `1.0584216659e-09` and its Newton seed has maximum absolute value `2.18601436637e-10`. Including the A384 point-Jacobian defect, its product-disk radius is `2.38409439399e-10`. Including the dependency-forgetting A386 residual widths raises that point-test radius to `0.00251620150315`.

The current A385S complex disk radius is `1.41421356237e-07`, which contains the floating seed, but the full A386 sufficient point test does not pass. This is not a nonexistence result: the whole-polydisk Jacobian is not yet transported, and the A386 residual still loses beta-period cancellation. The packet fixes the numerical scales for those two remaining constructions.

class Binding(object):
    def __init__(self, parent):
        self.parent = parent
        self.partner = None
    def bind(self, other):
        self.partner = other
        other.partner = self

class Monomer(object):
    def __init__(self, n_bindings):
        self.bindings = []
        for i in range(n_bindings):
            self.bindings.append(Binding(self))
    
    @property
    def free_bindings(self):
        return (b for b in self.bindings if b.partner is None)
        #return filter(lambda b: b.partner is None, self.bindings)

class Cell(Monomer):
    n_cells=0
    def __init__(self, n_bindings):
        super(Cell, self).__init__(n_bindings)
        self.id = self.n_cells
        Cell.n_cells += 1

class Protein(Monomer):
    n_proteins=0
    def __init__(self, n_bindings):
        super(Protein, self).__init__(n_bindings)
        self.id = self.n_proteins
        Protein.n_proteins += 1
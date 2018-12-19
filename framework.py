import random, time
random.seed(time.time())

class Gate:
  def __init__(self, method, conn1, conn2):
    self.__repr__ = lambda: method
    self.method_dict = {"and":self.And, "or":self.Or, 
                        "xor":self.Xor, "nand":self.NAnd,
                        "nor":self.NOr, "xnor":self.XNor,
                        "&":self.And, "|":self.Or,
                        "^":self.Xor, "!&":self.NAnd, 
                        "!|":self.Or, "!^":self.XNor}
    self.method = self.method_dict[method.lower()]
    self.conn1, self.conn2 = conn1, conn2

  def Not(self, inp):
    if inp == 0:
      return 1
    elif inp == 1:
      return 0

  def And(self, inp1, inp2):
    return inp1 & inp2

  def Or(self, inp1, inp2):
    return inp1 | inp2
  
  def Xor(self, inp1, inp2):
    return inp1 ^ inp2

  def NAnd(self, inp1, inp2):
    return self.Not(inp1 & inp2)

  def NOr(self, inp1, inp2):
    return self.Not(inp1 | inp2)
  
  def XNor(self, inp1, inp2):
    return self.Not(inp1 ^ inp2)

  def set_method(self, method):
    self.__repr__ = lambda: method
    self.method = self.method_dict[method.lower()]
  
  def activate(self, inputs):
    return self.method(inputs[self.conn1], inputs[self.conn2])

class Layer:
  def __init__(self, previous_n, minimum_gates=3, maximum_gates=10):
    self.methods = ["and", "or", "xor", "nand", "nor", "xnor"]
    self.previous_n = previous_n
    self.n_gates = random.randint(minimum_gates, maximum_gates)
    self.gate_methods = [random.choice(self.methods) for _ in range(self.n_gates)]
    self.gates = [Gate(method, *random.sample(range(previous_n), 2)) for method in self.gate_methods]

  def output_init(self, n_gates):
    self.n_gates = n_gates
    self.gate_methods = [random.choice(self.methods) for _ in range(self.n_gates)]
    self.gates = [Gate(method, random.randint(0, self.previous_n-1), random.randint(0, self.previous_n-1)) for method in self.gate_methods]

  def feed_forward(self, inputs):
    return [gate.activate(inputs) for gate in self.gates]

class LogicalNetwork:
  def __init__(self, layers_n, input_n, output_n):
    self.input_layer = Layer(input_n)
    self.layers = []
    latest = self.input_layer
    for _ in range(layers_n-1):
      self.layers.append(latest)
      latest = Layer(latest.n_gates)
    latest.output_init(output_n)
    self.layers.append(latest)

  def feed_forward(self, inputs):
    latest = self.layers[0].feed_forward(inputs)
    for layer in self.layers[1:]:
      latest = layer.feed_forward(latest)
    return latest

if __name__ == "__main__":
  LN = LogicalNetwork(layers_n = 3, input_n = 3, output_n = 3)
  print(LN.feed_forward([1, 0, 1]))
  for layer in LN.layers:
    for gate in layer.gates:
      print(gate.__repr__(), gate.conn1, gate.conn2)

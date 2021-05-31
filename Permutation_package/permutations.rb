#------------------
# Permutations
#------------------

#--------------------------------------------
class Permutation
  def initialize(image=(0..4).to_a)
    raise ArgumentError, "Not non-negative integers" unless image.all?{|v| v.is_a?(Integer) && (v >= 0)}
    raise ArgumentError, "Not a permutation of 0 to #{image.size}" unless image.sort == (0..image.size-1).to_a
    @size = image.size
    @image = image
  end
  attr_accessor :size, :image
#-----
  def act(arg)
#    raise ArgumentError, "#{self.show} can not act onto #{arg}" unless image.all?{|v| arg.include?(v)}
    raise ArgumentError, "Not non-negative integers" unless [arg].flatten.all?{|v| v.is_a?(Integer) && (v >= 0)}
    case arg
    when Integer
      return @image[arg].then{|v| (v.nil?) ? arg : v}
    when Array
      return arg.map{|v| self.act(v)}
    else
      raise ArgumentError, "Input an Integer or an Array!"
    end
  end
  def *(aPerm)
    raise ArgumentError, "Not a Permutation" unless aPerm.is_a?(Permutation)
    return Permutation.new(self.act(aPerm.image))
  end
#-----    
  def to_s
    "#{(0..@size-1).to_a}\n#{image}"
  end
  def inspect
    "(" + (0..@size-1).map{|i| "#{i}\u{21a6}#{image[i]}"}.join(',') + ")"
#    "(" + (0..@size-1).map{|i| "\u{21a6}#{image[i]}"}.join(',') + ")"
  end
  def display(before)
    "#{before}  |-#{self.inspect}->  #{self.act(before)}"
  end
end


#--------------------------------------------
class Cycle < Permutation
  def initialize(arg)
    @seq = arg
    @length = arg.size
    image = (0..arg.max).map do |k|
      ind = arg.index(k)
      (ind.nil?) ? k : arg[(ind+1)%arg.size]
    end
    super(image)
  end
  attr_accessor :length
#-----  
  def to_s
    "(#{@seq.join(',')})"
  end
  def inspect
    "(#{@seq.join("\u{21a6}")}\u{21a6})"
  end
end


#--------------------------------------------
class Transposition < Cycle
  def initialize(i,j)
    @pair = [i,j]
    super(@pair)
  end
#-----  
  def inspect
    "(#{@seq.join("\u{21c4}")})"
  end
end


#--------------------------------------------
def decompose(perm)
  seqs = []
  im = perm.image.dup
  while im.size > 0
    seq = [im.first]
    while seq.count(seq.first) == 1
      seq << perm.act(seq.last)
    end
    seq.pop
    seqs << Cycle.new(seq)
    seq.each{|v| im.delete(v)}
  end
  return seqs.sort_by{|a| a.length }
end
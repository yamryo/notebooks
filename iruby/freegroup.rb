# coding: utf-8

# # Free Group

#------------------------------------------------------------
module Element
  def initialize(factors = [])
    @factors = factors
  end
  attr_reader :factors
  #---
  def to_s() @factors.map(&:to_s).join end
  def show() self.to_s end
  def length() @factors.length end
  def ==(anElement) self.show == anElement.show end
end

#------------------------------------------------------------
class Letter
  include Element
  #---
  def initialize(char='1')
    raise ArgumentError, "You can use alphabet and '1'" unless char[0] =~ /[1a-zA-Z]/
    super([char])
    @char = char[0]
  end
  attr_reader :char
  #---
  def =~(a_Letter)
    raise ArgumentError unless a_Letter.is_a? Letter
    @char.downcase == a_Letter.char.downcase
  end
  def ==(a_Letter)
    raise ArgumentError unless a_Letter.is_a? Letter
    (self =~ a_Letter) && (self.inverse? == a_Letter.inverse?)
  end
  def ===(a_Letter)
    raise(ArgumentError) unless a_Letter.is_a? Letter
    self.object_id == a_Letter.object_id
  end
  def <=>(a_Letter)
    raise(ArgumentError) unless a_Letter.is_a? Letter
    self.show <=> another.show
  end
  #---
  def inverse
    if @char == '1' then
      self.dup
    else
      inv_char = (self.inverse?) ? @char.downcase : @char.upcase
      self.class.new(inv_char)
    end
  end
  def inverse?() (@char == '1') ? nil : (@char == @char.upcase) end
  def inverse_of?(a_Letter)
    (@char == '1') ? (a_Letter.char == '1') : (self =~ a_Letter) && !(self == a_Letter)
  end
end

#------------------------------------------------------------
class Word
  include Element
  #---
  # Word class consists of a (nested) array of Letter objects.
  #---
  def initialize(*args)
    args.flatten!
    @factors = []
    if args.empty?
      @factors << Letter.new('1')
    else
      args.each do |arg|
        @factors << case arg
                    when Letter then
                      arg
                    when String then
                      subarr = []
                      arg.each_char{|c| subarr << Letter.new(c) if c =~ /[1a-zA-Z]/}
                      if subarr.empty?
                        Letter.new('1')
                       elsif subarr.length == 1
                         subarr[0]
                      else
                        subarr
                      end
                    else raise ArgumentError 
                    end
      end
      @factors = @factors[0] if (@factors.length == 1 and @factors[0].is_a?(Array))
    end
#     super(factors)
  end
  attr_accessor :factors
  #---
  def pop() @factors.pop end
  def letter_at(int) @factors[int] end
  def [](int) self.letter_at(int) end
  #---
  def flatten
    flat_factors = @factors.flatten
    self.class.new(flat_factors)
  end
  def flatten!() @factors.flatten!; return self end
  #---
  def show() show_parens(@factors) end 
  def show_parens(myarr)
    myarr.map{|f| (f.is_a?(Array)) ? "(#{self.show_parens(f)})" : f.show }.join
  end
  #---
  def inverse
      return self.class.new(@factors.flatten.reverse.map(&:inverse))
  end
  def deep_copy
    facs_copy = []
    for f in @factors
      facs_copy << f
    end
    rtn = Word.new
    rtn.factors = facs_copy
    return rtn
  end
  #---
  def contract_once
#     self.flatten!
    rtn = [@factors[0]]
    @factors.each_cons(2) do |f1, f2|
      (f1 =~ f2 and f1 != f2) ? rtn.pop : rtn << f2
    end
    @factors = (rtn.empty?) ? [Letter.new('1')] : rtn 
    return self
  end
  def contract
    self.flatten!
    size_diff = 1
    while (size_diff > 0 and @factors.size > 1)
      size_diff = @factors.size - self.contract_once.factors.size
    end
    #
    return self
  end
  #---
  def cyclic_permutation(num=1)
    letters = @factors.flatten
    first = letters[0, num]
    second = letters.drop(num)
    return self.class.new(second + first)
  end
  #---
  def *(anElement)
    raise ArgumentError unless anElement.is_a? Element
    pd = self.dup
    pd.factors = [pd.factors, anElement.factors]
    #return self.class.new(self.show, anElement.show)
    return pd
  end
  def size
    return @factors.flatten.size
  end
end

#------------------------------------------------------------
module Group extend self
  Identity = Word.new('1')
  #---
  def product(element1,element2)
    raise ArgumentError unless [element1, element2].all?{|elm| elm.is_a? Element}
    return Word.new(element1.factors, element2.factors)
  end
end